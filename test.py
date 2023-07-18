class Plugin:
    def __init__(self, name):
        self.name = name

    def install(self):
        raise NotImplementedError

    def initialize(self):
        raise NotImplementedError

    def process(self, user_input):
        raise NotImplementedError


class MockPlugin(Plugin):
    def install(self):
        print(f"Installing {self.name}")

    def initialize(self):
        print(f"Initializing {self.name}")

    def process(self, user_input):
        print(f"Processing input: {user_input}")
        return f"Processed input: {user_input}"


class PluginManager:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, plugin):
        self.plugins[plugin.name] = plugin
        plugin.install()

    def initialize_plugin(self, plugin_name):
        self.plugins[plugin_name].initialize()

    def process_with_plugin(self, plugin_name, user_input):
        return self.plugins[plugin_name].process(user_input)


# Usage
plugin_manager = PluginManager()
mock_plugin = MockPlugin("MockPlugin")
plugin_manager.register_plugin(mock_plugin)
plugin_manager.initialize_plugin("MockPlugin")
plugin_manager.process_with_plugin("MockPlugin", "Hello, world!")
