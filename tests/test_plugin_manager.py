import unittest
from plugins.mock_plugin import MockPlugin
from plugins.plugin_manager import PluginManager

    
class test_plugin_manager(unittest.TestCase):
    def setUp(self):
        self.mock_plugin=MockPlugin("MockPlugin")
        self.plugin_manager=PluginManager()

    def test_register_plugin(self):
        self.plugin_manager.register_plugin(self.mock_plugin)
        self.assertEqual(len(self.plugin_manager.plugins), 1)

    def test_initialize_plugin(self):
        self.plugin_manager.register_plugin(self.mock_plugin)
        response = self.plugin_manager.initialize_plugin(plugin_name="MockPlugin")
        self.assertEqual(response, "Initializing MockPlugin")

    def test_process_with_plugin(self, user_input="Hello World!"):
        self.plugin_manager.register_plugin(self.mock_plugin)
        response = self.plugin_manager.process_with_plugin(plugin_name="MockPlugin", user_input=user_input)
        self.assertEqual(response, "Processed input: Hello World!")



if __name__ == "__main__":
    unittest.main()