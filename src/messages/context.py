import json
from pydantic import BaseModel, FilePath, field_validator
from typing import List, Optional, Dict, Union
from src.messages.create_messages import CreateMessage


class Message(BaseModel):
    role: str
    content: str


class Primer(BaseModel):
    message: Message


class Context(BaseModel):
    context: List[Message] = []
    history_path: FilePath = "src/static/message_history/message_history.json"
    primer_path: FilePath = "src/static/primers/primers.json"


class ContextWindow(Context):
    @field_validator("context", check_fields=True)
    def load_history(cls, v, values):
        if "history_path" in values:
            with open(values["history_path"], "r") as f:
                return json.loads(f.read())
        return v or []

    def add_message(self, message: Message) -> List[Message]:
        self.context.append(message)
        self.save_history(message)
        return self.context

    def save_history(self, message: Message) -> None:
        with open(self.history_path, "w") as f:
            f.write(json.dumps(self.context, default=lambda x: x.model_dump()))

    def get_recent_messages(self, count: int = 8) -> List[Message]:
        return self.context[-count:]

    def save_primer(self, message: Message) -> None:
        with open(self.primer_path, "r") as f:
            primer = json.loads(f.read())
        primer.append(message.model_dump())
        with open(self.primer_path, "w") as f:
            f.write(json.dumps(primer))

    def load_primer(self, primer_choice: Optional[int] = 0) -> Primer:
        with open(self.primer_path, "r") as f:
            primer = Primer(**json.loads(f.read())[primer_choice])
        return primer

    def create_context(
        self,
        content: str,
        role: Optional[str] = None,
        context_window: Optional[int] = None,
        primer_choice: Optional[int] = None,
    ) -> List[Message]:
        context_window = context_window or 8
        primer_choice = primer_choice or 0

        primer = self.load_primer(primer_choice)
        history = self.get_recent_messages(context_window)
        create_message = CreateMessage()
        user_message = create_message.create_message(role, content)
        self.save_history(user_message)
        self.context.append(primer.message)
        self.context.extend(history)
        self.context.append(user_message)
        return self.context
