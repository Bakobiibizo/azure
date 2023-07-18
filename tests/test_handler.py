import unittest
import base64
from src.data_handler import DataHandler


class TestCreateMessage(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.handler = DataHandler(persona_image="src/static/images/Eris0001.png")
        self.context = self.handler.context

    def test_handle_message(self):
        response = self.handler.handle_chat(role="user", content="hello, how are you?")
        self.assertEqual(response.choices[0]["message"]["role"], "assistant")

    def test_handle_image(self):
        result = self.handler.handle_image()
        with open(self.handler.image_path, "rb") as f:
            expected_result = base64.b64encode(f.read()).decode("utf-8")
        self.assertEqual(result, expected_result)