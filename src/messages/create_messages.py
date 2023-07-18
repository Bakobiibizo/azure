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

    def create_message(self, content: StrictStr, role=None) -> Dict[str, str]:
        role = self.verify_role(role)
        return Message(role=role, content=content).model_dump()

    def create_primer(self, content: StrictStr) -> Dict[str, Dict[str, str]]:
        message = self.create_message(role=RoleOptions.SYSTEM, content=content)
        return Primer(title="primer", message=message).model_dump()

    def verify_role(self, role):
        try:
            if not role:
                role = RoleOptions.USER
            if role == "user":
                return RoleOptions.USER
            if role == "assistant":
                return RoleOptions.ASSISTANT
            if role == "system":
                return RoleOptions.SYSTEM
        except Exception as e:
            raise ValueError(f"Role {role} is not valid: {e}")


def main():
    return CreateMessage()


if __name__ == "__main__":
    main()
