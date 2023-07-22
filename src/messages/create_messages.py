from src.messages.message_defs import Message, MessageType, RoleOptions


class Messages(Message):
    def __init__(self):
        pass
    
    def create_message(self, role: RoleOptions, content: str) -> Message:
        return Message(role=role, content=content)