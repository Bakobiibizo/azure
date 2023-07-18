from typing import List, Dict
from src.generation.openai_text import OpenAITextGeneration
from src.messages.context import ContextWindow
from src.messages.create_messages import CreateMessage
import base64
import json


class DataHandler:
    def __init__(self, persona_image=None):
        self.openai_text = OpenAITextGeneration()
        self.context_window = ContextWindow()
        self.image_path = persona_image
        self.context = self.context_window.context
        self.create_messages = CreateMessage()

    def handle_chat(self, role, content, context_window=None, primer_choice=None):
        if not self.context:
            self.context = self.context_window.create_context(
                role=role, content=content, context_window=context_window, primer_choice=primer_choice
                )
        else:
            message = self.create_messages.create_message(
                role=role, content=content
            )
            self.context = self.context_window.add_message(message)
        print(self.context)
        response = self.openai_text.send_chat_complete(self.context)
        self.context_window.save_history(response.choices[0]["message"])
        return response

    def handle_image(self):
        with open(self.image_path, "rb") as f:
            content = f.read()
        return base64.b64encode(content).decode("utf-8")
