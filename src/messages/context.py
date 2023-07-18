import os
import json
from pydantic import BaseModel, FilePath
from typing import List, Optional
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
    context_length: int = 10


class ContextWindow(Context):

    def load_history(self, primer_choice: Optional[int] = 8) -> List[Message]:
        self.context_length = primer_choice + 2
        with open(self.history_path, "r") as f:
            history = json.loads(f.read())
        if len(history) == 0: pass
        if len(history) <= primer_choice:
            return history
        else:
            return history[-primer_choice:]

    def add_message(self, message: Message) -> List[Message]:
        self.context.append(message)
        self.check_context_length(self.context)
        self.save_history(message)
        return self.context

    def save_history(self, message: Message) -> None:
        with open(self.history_path, "r") as f:
            history = json.loads(f.read())
        history.append(message)
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
            primer = Primer(**json.loads(f.read())[primer_choice]).model_dump()["message"]
        return primer

    def create_context(
        self,
        role: str,
        content: str,
        context_window: Optional[int] = None,
        primer_choice: Optional[int] = None,
    ) -> List[Message]:
        context_window = context_window or 8
        primer_choice = primer_choice or 0

        primer = self.load_primer(primer_choice)
        history = self.load_history(context_window)
        create_message = CreateMessage()
        user_message = create_message.create_message(role, content)
        self.save_history(user_message)
        self.context.append(primer)
        self.context.extend(history)
        self.context.append(json.loads(user_message))
        self.check_messages(self.context)

        print(self.context)
        return self.context

    def check_messages(self, messages: List[Message]) -> List[Message]:
        for message in messages:
            if not message["content"]:
                messages.remove(message)
        return messages

    def check_context_length(self, messages: List[Message]) -> List[Message]:
        if len(messages) > self.context_length:
            return messages[-self.context_length:]
        else:
            return messages
