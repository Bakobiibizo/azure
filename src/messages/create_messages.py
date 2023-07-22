from src.messages.message_defs import (
    Message, 
    RoleOptions
)
import json


class Messages:
    def __init__(self):
        pass
    
    def create_message(self, role: RoleOptions, content: str) -> Message:
        return Message(role=role, content=content)

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