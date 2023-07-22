import pytest
import hypothesis as hyp
from hypothesis import given, strategies
from hypothesis.strategies import  sampled_from, text
from pydantic import StrictStr
from src.messages.create_messages import Messages
from src.messages.message_defs import (
    RoleOptions,
    Message,
    MessageType,
    StoredMessage,
    HistoryMessages,
    PromptMessage,
    PrimerMessage,
    PromptChainMessage,
    PersonaMessage
)


class TestMessages:
    messages = Messages()

    @hyp.given(role=sampled_from(elements=list(RoleOptions)), content=text(min_size=1, max_size=100))
    def test_create_message(self, role, content) -> None:
        created_message = self.messages.create_message(role=role, content=content)
        assert role in RoleOptions
        assert isinstance(content, str)
        assert isinstance(created_message, Message)

    def test_message_to_json(self):
        created_message = self.messages.create_message(role=RoleOptions.USER, content="test")
        message_type = MessageType.HISTORY_MESSAGE
        message = HistoryMessages(message=created_message, message_type=message_type)
        json_str = self.messages.message_to_json(message)
        assert isinstance(json_str, str)

    def test_json_to_message(self):
        json_str = '{"message": {"role": "user", "content": "test"}, "message_type": "history_message"}'
        message = self.messages.json_to_message(json_str, MessageType.HISTORY_MESSAGE)
        assert isinstance(message, HistoryMessages)
        assert message.message.role == RoleOptions.USER
        assert message.message.content == "test"
        assert message.message_type == MessageType.HISTORY_MESSAGE

