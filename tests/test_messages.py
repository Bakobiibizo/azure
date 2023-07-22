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
from src.messages.create_messages import Messages


class TestMessages:
    global logger
    messages = Messages()

    @hyp.given(role=sampled_from(elements=list(RoleOptions)), content=text(min_size=1, max_size=100))
    def test_create_message(self, role, content) -> None:
        created_message = self.messages.create_message(role=role, content=content)
        assert role in RoleOptions
        assert isinstance(content, str)
        assert isinstance(created_message, Message)

