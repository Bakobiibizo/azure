#using the data shapes of the previous code you corrected can you please make this one compatable?
#you can ask me for clairifications or the data shapes again
import json
from pydantic import BaseModel
from data_converter import DataConverter
from conversions import Primer, Message
from typing import List, Optional


#array representing a file
message_history = []

#array representing a file
primers = []

class Context(BaseModel):
    context: List[Message]

class ContextManager():
    context: (List[Message])
    context_length: int
    converter: DataConverter
    history_path: str
    primer_path: str
    history: List[Message]


class ContextWindow(Context):
    def __init__(self):
        self.context = []
        self.context_length = 10
        self.converter = DataConverter()
        super().__init__(self, primer_choice=0)
        self.history_path = "src/static/message_history/message_history.json"
        self.primer_path = "src/static/primers/primers.json"
        self.context = self.converter.context
        self.history = self.converter.open(self.history_path)


    def load_history(self, context_window: Optional[int] = 8) -> None:
        if len(self.history) < context_window:
            self.context.extend(self.history)
        else:
            self.context.append(self.history[-context_window:])

    def add_message(self, message: Message) -> None:
        new_message = Message(message.role, message.content)
        self.save_history(new_message)
        self.context.append(new_message)
        self.check_context()
        self.get_context()

    def save_history(self, message: Message) -> None:
        self.history.append(message)

    def save_primer(self, primer: Primer) -> None:
        self.check_messages([primer.message])
        self.primers.append(primer)

    def load_primer(self, primer_choice: Optional[int] = 0) -> None:
        primer_message = self.context.insert(
            dict[
                self.primers[primer_choice]["message"]["role"],
                self.primers[primer_choice]["message"]["content"]
                ])
        self.context.append(primer_message)

    def create_context(self, 
                       user_message: Message, 
                       context_window: Optional[int] = 8, 
                       primer_choice: Optional[int] = 0
                       ) -> None:
        self.load_primer(primer_choice)
        self.load_history(context_window)
        self.add_message(user_message)
        self.check_context()
        self.check_messages()

    def check_context(self) -> None:
        self.context = [m for m in self.context[-self.context_length:]]

    def check_messages(self, messages: List[Message]) -> None:
        for message in messages:
            if message.role is None or message.content is None:
                raise ValueError("Message cannot have empty fields.")

    def get_context(self) -> List[Message]:
        return self.context

# Create ContextWindow instance
cw = ContextWindow()

# Create and add a message to the context
m1 = Message("user", "Hello, how are you?")
cw.add_message(m1)

# Print current context
print(f"Current context: {[m.__dict__ for m in cw.get_context()]}")

# Save a primer
p1 = Primer("greeting", m1)
cw.save_primer(p1)

# Add a new message and update the context with the new message, history, and a primer
m2 = Message("user", "What's the weather like?")
cw.add_message(m2)
cw.create_context(m2)

# Print updated context
print(f"Updated context: {[m.__dict__ for m in cw.get_context()]}")
