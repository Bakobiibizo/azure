class PluginManager:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, plugin):
        self.plugins[plugin.name] = plugin
        plugin.install()

    def initialize_plugin(self, plugin_name):
        return self.plugins[plugin_name].initialize()

    def process_with_plugin(self, plugin_name, user_input):
        return self.plugins[plugin_name].process(user_input)

