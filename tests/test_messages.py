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

    def test_stored_message_to_json(self):
        created_message = self.messages.create_message(role=RoleOptions.USER, content="test")
        message = StoredMessage(message=created_message)
        json_str = self.messages.stored_message_to_json(message)
        assert isinstance(json_str, str)

    def test_json_to_stored_message(self):
        json_str = '{"message": {"role": "user", "content": "test"}}'
        message = self.messages.json_to_stored_message(json_str)
        assert isinstance(message, StoredMessage)
        assert message.message.role == RoleOptions.USER
        assert message.message.content == "test"

    def test_primer_message_to_json(self):
        created_message = self.messages.create_message(role=RoleOptions.USER, content="test")
        message = PrimerMessage(message=created_message, message_title="test title")
        json_str = self.messages.primer_message_to_json(message)
        assert isinstance(json_str, str)

    def test_json_to_primer_message(self):
        json_str = '{"message": {"role": "user", "content": "test"}, "message_title": "test title"}'
        message = self.messages.json_to_primer_message(json_str)
        assert isinstance(message, PrimerMessage)
        assert message.message.role == RoleOptions.USER
        assert message.message.content == "test"
        assert message.message_title == "test title"

    def test_prompt_message_to_json(self):
        created_message = self.messages.create_message(role=RoleOptions.USER, content="test")
        message = PromptMessage(message=created_message, message_title="test title")
        json_str = self.messages.prompt_message_to_json(message)
        assert isinstance(json_str, str)

    def test_json_to_prompt_message(self):
        json_str = '{"message": {"role": "user", "content": "test"}, "message_title": "test title"}'
        message = self.messages.json_to_prompt_message(json_str)
        assert isinstance(message, PromptMessage)
        assert message.message.role == RoleOptions.USER
        assert message.message.content == "test"
        assert message.message_title == "test title"

    def test_prompt_chain_message_to_json(self):
        created_message = self.messages.create_message(role=RoleOptions.USER, content="test")
        message = PromptChainMessage(message=created_message, message_title="test title", message_description="test description")
        json_str = self.messages.prompt_chain_message_to_json(message)
        assert isinstance(json_str, str)

    def test_json_to_prompt_chain_message(self):
        json_str = '{"message": {"role": "user", "content": "test"}, "message_title": "test title", "message_description": "test description"}'
        message = self.messages.json_to_prompt_chain_message(json_str)
        assert isinstance(message, PromptChainMessage)
        assert message.message.role == RoleOptions.USER
        assert message.message.content == "test"
        assert message.message_title == "test title"
        assert message.message_description == "test description"

    def test_persona_message_to_json(self):
        created_message = self.messages.create_message(role=RoleOptions.USER, content="test")
        message = PersonaMessage(message=created_message)
        json_str = self.messages.persona_message_to_json(message)
        assert isinstance(json_str, str)

    def test_json_to_persona_message(self):
        json_str = '{"message": {"role": "user", "content": "test"}}'
        message = self.messages.json_to_persona_message(json_str)
        assert isinstance(message, PersonaMessage)
        assert message.message.role == RoleOptions.USER
        assert message.message.content == "test"

