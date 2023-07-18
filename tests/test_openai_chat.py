import unittest
from src.generation.openai_text import OpenAITextGeneration


class TestOpenAITextGeneration(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_send_chat_complete(self):
        openai_text_gen = OpenAITextGeneration()
        response = openai_text_gen.send_chat_complete(
            messages=[
                {
                    "role": "user",
                    "content": "Write me a haiku about a duck wearing a fedora",
                }
            ]
        )
        self.assertEqual(response.choices[0].message["role"], "assistant")
