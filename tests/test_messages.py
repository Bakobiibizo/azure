import json
import hypothesis as hyp
from typing import Dict
from hypothesis.strategies import  sampled_from, text
from src.system_tools.logger import LoggerInstance
from src.messages.create_messages import Messages
from src.messages.message_defs import (
    RoleOptions,
    Message,
    MessageType,
    HistoryMessage,
    PromptMessage,
    PrimerMessage,
    PromptChainMessage,
    PersonaMessage
)
instance = LoggerInstance()
logger = instance.get_logger()
logger.log("Initialized test_messages:\n")

class TestMessages:
    def setup_method(self):
        self.messages = Messages()
        self.message_type = MessageType

    @hyp.given(role=sampled_from(elements=list(RoleOptions)), content=text(min_size=1, max_size=100))
    def test_create_message(self, role, content) -> None:
        created_message = self.messages.create_message(role=role, content=content)
        assert created_message.role == role
        assert created_message.content == content
        assert isinstance(created_message, Message)

    def test_message_to_json(self):
        role = RoleOptions.USER
        content = "test"
        message = dict(role=role, content=content)
        json_str = self.messages.message_to_json(message)
        assert isinstance(json_str, str)
        assert json.loads(json_str)["role"] == RoleOptions.USER.value
        assert json.loads(json_str)["content"] == "test"

    def test_json_to_message(self):
        json_str = '{"role": "user", "content": "test"}'
        message = self.messages.json_to_message(json_str)
        assert message["role"], json_str.role
        assert message["content"], json_str.content

    def test_history_message_to_json(self):
        json = {"message": {"role": "user", "content": "test"}, "message_type": "history_message"}
        created_message = self.messages.create_message(role=RoleOptions.USER, content="test")
        message = HistoryMessage(message=created_message, message_type=MessageType.HISTORY_MESSAGE)
        json_str = self.messages.history_message_to_json(message)
        assert json_str, json

#    def test_json_to_history_message(self):
#        json_str = '{"message_type: "history_message", "message": {"message": {"role": "user", "content": "test"}'
#        msg = HistoryMessage(json_str)
#        message = self.messages.json_to_history_message(json_str)
#        assert(message, msg)
#        assert message.message.role == RoleOptions.USER
#        assert message.message.content == "test"
#
#    def test_primer_message_to_json(self):
#        created_message = self.messages.create_message(role=RoleOptions.USER, content="test")
#        message = PrimerMessage(message=created_message, message_type=MessageType.PRIMER_MESSAGE, message_title="test title",)
#        json_str = self.messages.primer_message_to_json(message)
#        assert isinstance(json_str, str)
#
#    def test_json_to_primer_message(self):
#        json_str = '{"message": {"role": "user", "content": "test"}, "message_title": "test title"}'
#        message = self.messages.json_to_primer_message(json_str)
#        assert isinstance(message, PrimerMessage)
#        assert message.message.role == RoleOptions.USER
#        assert message.message.content == "test"
#        assert message.message_title == "test title"
#
#    def test_prompt_message_to_json(self):
#        created_message = self.messages.create_message(role=RoleOptions.USER, content="test")
#        message = PromptMessage(message=created_message, message_type=MessageType.PROMPT_MESSAGE, message_title="test title")
#        json_str = self.messages.prompt_message_to_json(message)
#        assert isinstance(json_str, str)
#
#    def test_json_to_prompt_message(self):
#        json_str = '{"message": {"role": "user", "content": "test"}, "message_title": "test title"}'
#        message = self.messages.json_to_prompt_message(json_str)
#        assert isinstance(message, PromptMessage)
#        assert message.message.role == RoleOptions.USER
#        assert message.message.content == "test"
#        assert message.message_title == "test title"
#
#    def test_prompt_chain_message_to_json(self):
#        created_message = self.messages.create_message(role=RoleOptions.USER, content="test")
#        message = PromptChainMessage(message=created_message, message_type=MessageType.PROMPT_CHAIN_MESSAGE, message_title="test title", message_description="test description")
#        json_str = self.messages.prompt_chain_message_to_json(message=message)
#        assert isinstance(json_str, str)
#
#    def test_json_to_prompt_chain_message(self):
#        json_str = '{"message": {"role": "user", "content": "test"}, "message_title": "test title", "message_description": "test description"}'
#        message = self.messages.json_to_prompt_chain_message(json_str)
#        assert isinstance(message, PromptChainMessage)
#        assert message.message.role == RoleOptions.USER
#        assert message.message.content == "test"
#        assert message.message_title == "test title"
#        assert message.message_description == "test description"
#
#    def test_persona_message_to_json(self):
#        created_message = self.messages.create_message(role=RoleOptions.USER, content="test")
#        message = PersonaMessage(message=created_message, message_type=MessageType.PERSONA_MESSAGE)
#        json_str = self.messages.persona_message_to_json(message)
#        assert isinstance(json_str, str)
#
#    def test_json_to_persona_message(self):
#        json_str = '{"message": {"role": "user", "content": "test"}, "message_type": "persona_message"}'
#        message = self.messages.json_to_persona_message(json_str)
#        assert isinstance(message, PersonaMessage)
#        assert message.message.role == RoleOptions.USER
#        assert message.message.content == "test"
#        assert message.message_type == MessageType.PERSONA_MESSAGE
#
#