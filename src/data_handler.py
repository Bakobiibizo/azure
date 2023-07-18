from src.generation.openai_text import OpenAITextGeneration
from src.messages.context import ContextWindow
import base64


class DataHandler:
    def __init__(self, persona_image=None):
        self.openai_text = OpenAITextGeneration()
        self.context_window = ContextWindow()
        self.image_path = persona_image
        self.context = self.context_window.context

    def handle_chat(self, content, role=None, context_window=None, primer_choice=None):
        if not self.context:
            self.context = self.context_window.create_context(
                role, content, primer_choice, context_window
            )
        else:
            self.context = self.context_window.add_context(content)
        print(self.context)
        response = self.openai_text.send_chat_complete(self.context).choices[0][
            "message"
        ]
        self.context_window.save_history(response)
        return response

    def handle_image(self):
        with open(self.image_path, "rb") as f:
            content = f.read()
        return base64.b64encode(content).decode("utf-8")
