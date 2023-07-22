from src.plugins.plugin import Plugin


class MockPlugin(Plugin):
    def install(self):
        print(f"Installing {self.name}")

    def initialize(self):
        print(f"Initializing {self.name}")
        return(f"Initializing {self.name}")

    def process(self, user_input):
        print(f"Processing input: {user_input}")
        return f"Processed input: {user_input}"