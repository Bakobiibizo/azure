from pydantic import BaseModel, StrictStr
from enum import Enum


class RoleOptions(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"

class Message(BaseModel):
    role: RoleOptions
    content: StrictStr

class MessageType(str, Enum):
    HISTORY_MESSAGE = "history_message"
    PRIMER_MESSAGE = "primer_message"
    PROMPT_MESSAGE = "prompt_message"
    CHAIN_MESSAGE = "chain_message"
    PERSONA_MESSAGE = "persona_message"

class StoredMessage(BaseModel):
    message: Message


    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            MessageType: lambda v: v.value,
        }

from pydantic import validator

class HistoryMessages(StoredMessage):
    message_type: str

    @validator('message_type', pre=True, always=True)
    def set_message_type(cls, v):
        return MessageType.HISTORY_MESSAGE.value

class PrimerMessage(StoredMessage):
    message_type: MessageType.PRIMER_MESSAGE
    message_title: StrictStr

class PromptMessage(StoredMessage):
    message_type: MessageType.PROMPT_MESSAGE
    message_title: StrictStr

class PromptChainMessage(StoredMessage):
    message_type: MessageType.PROMPT_MESSAGE
    message_title: StrictStr
    message_description: StrictStr

class PersonaMessage(StoredMessage):
    message_type: MessageType.PERSONA_MESSAGE

