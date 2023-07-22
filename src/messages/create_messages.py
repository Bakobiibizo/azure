from src.messages.message_defs import Message, MessageType, RoleOptions, StoredMessage, HistoryMessages, PrimerMessage, PromptMessage, PromptChainMessage, PersonaMessage
import json


class Messages:
    def __init__(self):
        pass
    
    def create_message(self, role: RoleOptions, content: str) -> Message:
        return Message(role=role, content=content)

    def message_to_json(self, message: StoredMessage) -> str:
        return message.json()

    def json_to_message(self, json_str: str, message_type: MessageType) -> StoredMessage:
        if message_type == MessageType.HISTORY_MESSAGE:
            return HistoryMessages.parse_raw(json_str)
        elif message_type == MessageType.PRIMER_MESSAGE:
            return PrimerMessage.parse_raw(json_str)
        elif message_type == MessageType.PROMPT_MESSAGE:
            return PromptMessage.parse_raw(json_str)
        elif message_type == MessageType.CHAIN_MESSAGE:
            return PromptChainMessage.parse_raw(json_str)
        elif message_type == MessageType.PERSONA_MESSAGE:
            return PersonaMessage.parse_raw(json_str)
        else:
            raise ValueError("Invalid message type")

    def stored_message_to_json(self, message: StoredMessage) -> str:
        return message.json()

    def json_to_stored_message(self, json_str: str) -> StoredMessage:
        return StoredMessage.parse_raw(json_str)

    def primer_message_to_json(self, message: PrimerMessage) -> str:
        return message.json()

    def json_to_primer_message(self, json_str: str) -> PrimerMessage:
        return PrimerMessage.parse_raw(json_str)

    def prompt_message_to_json(self, message: PromptMessage) -> str:
        return message.json()

    def json_to_prompt_message(self, json_str: str) -> PromptMessage:
        return PromptMessage.parse_raw(json_str)

    def prompt_chain_message_to_json(self, message: PromptChainMessage) -> str:
        return message.json()

    def json_to_prompt_chain_message(self, json_str: str) -> PromptChainMessage:
        return PromptChainMessage.parse_raw(json_str)

    def persona_message_to_json(self, message: PersonaMessage) -> str:
        return message.json()

    def json_to_persona_message(self, json_str: str) -> PersonaMessage:
        return PersonaMessage.parse_raw(json_str)