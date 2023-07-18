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
    message: str
    title: str


class CreateMessage(Message):
    def __init__(self):
        print(f"Creating a Message instance: {Message}")
        print(f"Creating a Message instance: {Primer}")
        print(f"Creating a RoleOptions instance: {RoleOptions}")

    def create_message(self, role, content: StrictStr, ) -> str:
        role = self.verify_role(role)
        return Message(role=role, content=content).model_dump_json()

    def create_primer(self, content: StrictStr) -> str:
        message = self.create_message(role=RoleOptions.SYSTEM, content=content)
        return Primer(title="primer", message=message).model_dump_json()

    def verify_role(self, role) -> RoleOptions:
        if role == "user":
            return RoleOptions.USER
        if role == "assistant":
            return RoleOptions.ASSISTANT
        if role == "system":
            return RoleOptions.SYSTEM
        else:
            return RoleOptions.USER
