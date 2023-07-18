import unittest
from src.data_handler import DataHandler


class TestCreateMessage(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.handler = DataHandler()
        self.context = self.handler.context

    def test_handle_message(self):
        response = self.handler.handle_chat(role="user", content="hello, how are you?")
        self.assertEqual(response["role"], "assistant")
