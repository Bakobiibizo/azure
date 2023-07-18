import os
import json
import unittest
from src.messages.context import ContextWindow, Message


class TestContextWindow(unittest.TestCase):
    def setUp(self):
        self.context_window = ContextWindow()
        self.sample_message = Message(role="user", content="Hello, world!")

    def test_add_message(self):
        initial_length = len(self.context_window.context)
        self.context_window.add_message(self.sample_message)
        self.assertEqual(len(self.context_window.context), initial_length + 1)
        self.assertEqual(self.context_window.context[-1], self.sample_message)

    def test_save_history(self):
        self.context_window.add_message(self.sample_message)
        self.context_window.save_history(self.sample_message)
        with open(self.context_window.history_path, "r") as f:
            history = json.load(f)
        self.assertEqual(len(history), len(self.context_window.context))
        self.assertEqual(history[-1], self.sample_message.model_dump())

    def test_get_recent_messages(self):
        self.context_window.context.extend([self.sample_message] * 10)
        recent_messages = self.context_window.get_recent_messages(5)
        self.assertEqual(len(recent_messages), 5)
        self.assertEqual(recent_messages[0], self.sample_message)

    def test_create_context(self):
        self.context_window.create_context(content="Hello, world!")
        self.assertEqual(self.context_window.context[-1], '{"role":"user","content":"Hello, world!"}')

    def tearDown(self):
        # Clean up the history file after each test
        with open(self.context_window.history_path, "w") as f:
            json.dump([], f)


if __name__ == "__main__":
    unittest.main()
