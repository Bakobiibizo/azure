from typing import Dict
from enum import Enum
from pydantic import BaseModel, StrictStr


class RoleOptions(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


class Message(BaseModel):
    role: RoleOptions
    content: StrictStr


class Primer(BaseModel):
    message: Dict[str, str]
    title: str


class CreateMessage(Message):
    def __init__(self):
        print(f"Creating a Message instance: {Message}")
        print(f"Creating a Message instance: {Primer}")
        print(f"Creating a RoleOptions instance: {RoleOptions}")

    def create_message(self, role: RoleOptions, content: StrictStr) -> Dict[str, str]:
        return Message(role=role, content=content).model_dump()

    def create_primer(self, content: StrictStr) -> Dict[str, Dict[str, str]]:
        message = self.create_message(role=RoleOptions.SYSTEM, content=content)
        return Primer(title="primer", message=message).model_dump()


def main():
    return CreateMessage()


if __name__ == "__main__":
    main()
