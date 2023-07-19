import json
import unittest
from src.messages.data_converter import DataConverter

class TestDataConverter(unittest.TestCase):
    def setUp(self):
        self.converter = DataConverter()

    def test_chain_to_json(self):
       data = self.converter.chain_to_json(self.converter.chain_objects)
       print(data)
       self.assertEqual(data, self.converter.chain_json_data)

    def test_primer_to_json(self):
       data = self.converter.primer_to_json(self.converter.primer_objects)
       print(data)
       self.assertEqual(data, self.converter.primer_json_data)

    def test_persona_to_json(self):
       data = self.converter.persona_to_json(self.converter.persona_objects)
       print(data)
       self.assertEqual(data, self.converter.persona_json_data)

    def test_message_history_to_json(self):
       data = self.converter.message_history_to_json(self.converter.message_history_objects)
       print(data)
       self.assertEqual(data, self.converter.message_history_json_data)

    def test_json_to_chain(self):
       data = self.converter.json_to_chain(self.converter.chain_json_data)
       print(data)
       self.assertEqual(data[0].prompt_chain_title, self.converter.chain_objects[0].prompt_chain_title)

    def test_json_to_primer(self):
       data = self.converter.json_to_primer(self.converter.primer_json_data)
       print(data)
       self.assertEqual(data[0].message.role, self.converter.primer_objects[0].message.role)

    def test_json_to_persona(self):
       data = self.converter.json_to_persona(self.converter.persona_json_data)
       print(data)
       self.assertEqual(data[0].message.role, self.converter.persona_objects[0].message.role)

    def test_json_to_message_history(self):
       data = self.converter.json_to_message_history(self.converter.message_history_json_data)
       print(data)
       self.assertEqual(data[0].message.role, self.converter.message_history_objects[0].message.role)

if __name__ == '__main__':
    unittest.main()