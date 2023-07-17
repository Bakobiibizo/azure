import json
from pydantic import BaseModel
from typing import List, Dict, Union


class Context(BaseModel):
    context: List[Dict[str, str]] = []
    history_path: str = "src/static/message_history/message_history.json"
    primer_path: str = "src/static/primers/primers.json"


class ContextWindow(Context):
    def __init__(self):
        super().__init__()
        self.context = []

    def add_context(self, message: Dict[str, str]) -> List[Dict[str, str]]:
        self.context.append(message)
        return self.context

    def save_history(self, message: Dict[str, str]) -> None:
        with open(self.history_path, "w") as f:
            f.write(json.dumps(message))

    def load_history(self, context_window: int) -> Union[List[Dict[str, str]], None]:
        with open(self.history_path, "r") as f:
            history_context = json.loads(f.read())
        if context_window <= 0:
            pass
        elif context_window >= len(history_context):
            return history_context
        else:
            return history_context[-context_window:]

    def save_primer(self, message: Dict[str, str]) -> None:
        with open(self.primer_path, "w") as f:
            f.write(json.dumps(message))

    def load_primer(self, primer_choice):
        if primer_choice is None:
            #  TODO attach this to the choice selector
            choice = 0
        else:
            raise NotImplementedError("Choice was not implimented")
        with open(self.primer_path, "r") as f:
            self.context.append(json.loads(f.read())[choice])


def main():
    return ContextWindow()
    # test()


def test():
    cm = CreateMessage()
    message = cm.create_message(role=RoleOptions.user, content="Hello, Assistant!")
    cw = ContextWindow(**message)
    cw.save_history(message)
    cw.load_history(1)

    with open("server/static/message_history/message_history.json", "r") as f:
        message = json.loads(f.read())[-1]
        cw.save_history(message)
        cw.load_history(1)
        print(cw.context)
        print(message)


if __name__ == "__main__":
    main()
