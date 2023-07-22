from src.messages.message_defs import (
    Message, 
    MessageType, 
    RoleOptions, 
    HistoryMessage, 
    PrimerMessage, 
    PromptMessage, 
    PromptChainMessage, 
    PersonaMessage
)
import json


class Messages:
    def __init__(self):
        pass
    
    def create_message(self, role: RoleOptions, content: str) -> Message:
        return Message(role=role, content=content)

    def message_to_json(self, message: Message) -> str:
        return message.json()
    
    def json_to_message(self, json_str: str) -> Message:
        return Message.parse_raw(json_str)

    def history_message_to_json(self, message: HistoryMessage) -> str:
        return message.json()

    def json_to_history_message(self, json_str: str) -> HistoryMessage:
        return HistoryMessage.parse_raw(json_str)

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

    def prompts_to_json(self, prompts: list) -> str:
        return json.dumps(prompts)

    def json_to_prompts(self, json_str: str) -> list:
        return json.loads(json_str)

    def chains_to_json(self, chains: list) -> str:
        return json.dumps(chains)

    def json_to_chains(self, json_str: str) -> list:
        return json.loads(json_str)

    def primers_to_json(self, primers: list) -> str:
        return json.dumps(primers)

    def json_to_primers(self, json_str: str) -> list:
        return json.loads(json_str)

    def personas_to_json(self, personas: list) -> str:
        return json.dumps(personas)

    def json_to_personas(self, json_str: str) -> list:
        return json.loads(json_str)

    def message_history_to_json(self, message_history: list) -> str:
        return json.dumps(message_history)

    def json_to_message_history(self, json_str: str) -> list:
        return json.loads(json_str)

    def message_to_json(self, message: dict) -> str:
        return json.dumps(message)

    def json_to_message(self, json_str: str) -> dict:
        return json.loads(json_str)