import json
import unittest
from src.messages.create_messages import CreateMessage, RoleOptions


class TestCreateMessage(unittest.TestCase):
    def setUp(self):
        self.create_messages = CreateMessage()

    def test_create_message(self):
        message = self.create_messages.create_message(
            role="user", content="Hello, assistant."
        )
        self.assertEqual(
            json.loads(message)["content"], "Hello, assistant."
        )
        message = self.create_messages.create_message(
            role="system", content="This is a system message"
        )
        self.assertEqual(
            json.loads(message)["role"], "system"
        )
        message = self.create_messages.create_message(
            role="assistant", content="This is an assitant speaking"
        )
        self.assertTrue(json.loads(message)["content"] == "This is an assitant speaking")

        message = self.create_messages.create_primer(content="Hello, system")
        self.assertEqual(
           json.loads(message)["title"], "primer")
        message = self.create_messages.create_primer("This is a system message")
        self.assertEqual(
            json.loads(message)["message"], json.dumps({"role": "system", "content": "This is a system message"}, default=lambda x: x.dict(), separators=(',', ':')))
            


if __name__ == "__main__":
    unittest.main(argv=[""], exit=False)
