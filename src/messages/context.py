import json
from pydantic import BaseModel
from typing import List, Dict, Union
from src.messages.create_messages import CreateMessage


class Context(BaseModel):
    context: List[Dict[str, str]] = []
    history_path: str = "src/static/message_history/message_history.json"
    primer_path: str = "src/static/primers/primers.json"


class ContextWindow(Context):
    def __init__(self):
        super().__init__()

    def add_context(self, message: Dict[str, str]) -> List[Dict[str, str]]:
        self.context.append(message)
        self.save_history(message)
        return self.context

    def save_history(self, message: Dict[str, str]) -> None:
        with open(self.history_path, "r") as f:
            history = json.loads(f.read())
        history.append(message)
        with open(self.history_path, "w") as f:
            f.write(json.dumps(history))

    def load_history(
        self, context_window: int = None
    ) -> Union[List[Dict[str, str]], None]:
        if not context_window:
            context_window = 8
        with open(self.history_path, "r") as f:
            history_context = json.loads(f.read())

        if len(history_context) <= 0:
            return None

        if len(history_context) >= context_window:
            return history_context[-context_window:]

        return history_context

    def save_primer(self, message: Dict[str, str]) -> None:
        with open(self.primer_path, "r") as f:
            primer = json.loads(f.read())
        primer.append(message)
        with open(self.primer_path, "w") as f:
            f.write(json.dumps(primer))

    def load_primer(self, primer_choice):
        if primer_choice is None:
            #  TODO attach this to the choice selector
            primer_choice = 0
        with open(self.primer_path, "r") as f:
            primer = json.loads(f.read())[primer_choice]
        return primer

    def create_context(
        self, content, role=None, context_window=None, primer_choice=None
    ):
        primer = self.load_primer(primer_choice)
        history = self.load_history(context_window)
        create_message = CreateMessage()
        user_message = create_message.create_message(role, content)
        self.save_history(user_message)
        self.context.append(primer["message"])
        for message in history:
            self.context.append(message)
        self.context.append(user_message)
        return self.context


def main():
    return ContextWindow()
    # test()


if __name__ == "__main__":
    main()
