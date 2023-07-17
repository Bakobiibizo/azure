import json
import unittest

from src.messages.context import ContextWindow


class TestContextWindow(unittest.TestCase):
    def setUp(self):
        self.context_window = ContextWindow()

    def tearDown(self):
        pass

    def test_add_context(self):
        message = {"key": "value"}
        self.context_window.add_context(message)
        self.assertEqual(self.context_window.context[-1], message)

    def test_save_history(self):
        message = {"key": "value"}
        self.context_window.save_history(message)
        with open(self.context_window.history_path, "r") as f:
            saved_message = json.load(f)
        self.assertEqual(saved_message, message)

    def test_load_history(self):
        message = {"key": "value"}
        with open(self.context_window.history_path, "w") as f:
            json.dump([message], f)
        loaded_history = self.context_window.load_history(1)
        self.assertEqual(loaded_history, [message])

    def test_save_primer(self):
        message = {"key": "value"}
        self.context_window.save_primer(message)
        with open(self.context_window.primer_path, "r") as f:
            saved_message = json.load(f)
        self.assertEqual(saved_message, message)

    def test_load_primer(self):
        with self.assertRaises(NotImplementedError):
            self.context_window.load_primer("primer_choice")


if __name__ == "__main__":
    unittest.main()
