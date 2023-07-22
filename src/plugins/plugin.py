class Plugin:
    def __init__(self, name):
        self.name = name

    def install(self):
        raise NotImplementedError

    def initialize(self):
        raise NotImplementedError

    def process(self, user_input):
        raise NotImplementedError