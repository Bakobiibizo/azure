import unittest
from src.generation.openai_text import OpenAITextGeneration
from openai.openai_response import OpenAIResponse


class TestOpenAITextGeneration(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_send_chat_complete(self):
        openai_text_gen = OpenAITextGeneration()
        responses = openai_text_gen.send_chat_complete(
            messages=[
                {
                    "role": "user",
                    "content": "Write me a haiku about a duck wearing a fedora",
                }
            ]
        )
        full_response = "".join(
            response.choices[0].delta.get("content", "") for response in responses
        )
        self.assertTrue(isinstance(full_response, str))

