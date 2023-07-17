import json
import unittest
from src.messages.create_messages import CreateMessage, RoleOptions


class TestCreateMessage(unittest.TestCase):
    def setUp(self):
        self.create_messages = CreateMessage()

    def test_create_message(self):
        message = self.create_messages.create_message(
            RoleOptions.USER, "Hello, assistant."
        )
        self.assertEqual(
            json.dumps(message), '{"role": "user", "content": "Hello, assistant."}'
        )
        message = self.create_messages.create_message(
            RoleOptions.SYSTEM, "This is a system message"
        )
        self.assertEqual(
            json.dumps(message),
            '{"role": "system", "content": "This is a system message"}',
        )
        message = self.create_messages.create_message(
            RoleOptions.ASSISTANT, "This is an assitant speaking"
        )
        self.assertEqual(
            json.dumps(message),
            '{"role": "assistant", "content": "This is an assitant speaking"}',
        )
        message = self.create_messages.create_primer(content="Hello, system")
        self.assertEqual(
            json.dumps(message),
            '{"message": {"role": "system", "content": "Hello, system"}, "title": "primer"}',
        )
        message = self.create_messages.create_primer("This is a system message")
        self.assertEqual(
            json.dumps(message),
            '{"message": {"role": "system", "content": "This is a system message"}, "title": "primer"}',
        )


if __name__ == "__main__":
    unittest.main(argv=[""], exit=False)
