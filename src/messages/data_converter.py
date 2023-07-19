import json

class Message:
    def __init__(self, role, content):
        self.role = role
        self.content = content

class Prompt:
    def __init__(self, prompt_title, message):
        self.prompt_title = prompt_title
        self.message = message

class Chain:
    def __init__(self, message=None, prompt_chain_title=None):
        self.prompt_chain_title = prompt_chain_title
        self.message = message if message else None

class Primer:
    def __init__(self, primer_title, message):
        self.primer_title = primer_title
        self.message = message

class Persona:
    def __init__(self, persona_title, description, image, message):
        self.persona_title = persona_title
        self.description = description
        self.image = image
        self.message = message

class MessageHistory:
    def __init__(self, message):
        self.message = message

def json_to_object(json_object, object_type):
    if object_type == 'Prompt':
        return Prompt(prompt_title=json_object["prompt_title"], message=json_object["message"])
    elif object_type == 'Chain':
        return Chain(message=json_object.get("message"), prompt_chain_title=json_object.get("prompt_chain_title"))
    elif object_type == 'Primer':
        return Primer(primer_title=json_object["primer_title"], message=json_object["message"])
    elif object_type == 'Persona':
        return Persona(persona_title=json_object["persona_title"], description=json_object["description"], image=json_object["image"], message=json_object["message"])
    elif object_type == 'MessageHistory':
        return MessageHistory(message=json_object)

def object_to_json(obj):
    if isinstance(obj, Message):
        return obj.__dict__
    if isinstance(obj, (Prompt, Chain, Primer, Persona, MessageHistory)):
        return {key: object_to_json(value) for key, value in obj.__dict__.items()}

def json_to_prompt(json_object):
    return Prompt(prompt_title=json_object["prompt_title"], message=json_object)

def prompt_to_json(prompt_obj):
    return {
        "prompt_title": prompt_obj.prompt_title,
        "message": object_to_json(prompt_obj.message)
    }

def json_to_chain(json_object):
    return Chain(message=json_object, prompt_chain_title=json_object.get("prompt_chain_title"))

def chain_to_json(chain_obj):
    chain_dict = {}
    if chain_obj.prompt_chain_title:
        chain_dict["prompt_chain_title"] = chain_obj.prompt_chain_title
    if chain_obj.message:
        chain_dict["message"] = object_to_json(chain_obj)
    return chain_dict

# Primer
def json_to_primer(json_object):
    return Primer(primer_title=json_object["primer_title"], message=json_object)

def primer_to_json(primer_obj):
    return {
        "primer_title": primer_obj.primer_title,
        "message": object_to_json(primer_obj)
    }

def json_to_persona(json_object):
    return Persona(persona_title=json_object["persona_title"], description=json_object["description"], image=json_object["image"], message=json_object)

def persona_to_json(persona_obj):
    return {
        "persona_title": persona_obj.persona_title,
        "description": persona_obj.description,
        "image": persona_obj.image,
        "message": object_to_json(persona_obj)
    }

def json_to_message_history(json_object):
    return MessageHistory(message={json_object["role"],json_object["context"]})

def message_history_to_json(message_history_obj):
    return {
        "message": message_history_obj
    }


class DataConverter():
    def __init__(self):
        self.chain_path = "src/static/prompt_chains/chains.json"
        self.primer_path = "src/static/primers/primers.json"
        self.persona_path = "src/static/personas/personas.json"
        self.message_history_path = "src/static/message_history/message_history.json"
        self.chain_json_data = self.open_json_file(file_name=self.chain_path)
        self.primer_json_data = self.open_json_file(file_name=self.primer_path)
        self.persona_json_data = self.open_json_file(file_name=self.persona_path)
        self.message_history_json_data = self.open_json_file(file_name=self.message_history_path)
        self.chain_objects = self.json_to_chain(chain_json_data=self.chain_json_data)
        self.primer_objects = self.json_to_primer(primer_json_data=self.primer_json_data)
        self.persona_objects = self.json_to_persona(persona_json_data=self.persona_json_data)
        self.message_history_objects = self.json_to_message_history(message_history_json_data=self.message_history_json_data)


    def open_json_file(self, file_name):
        with open(file_name, "r") as json_file:
            return json.load(json_file)
    def json_to_chain(self, chain_json_data):
        return [json_to_chain(item) for item in chain_json_data]
    def json_to_primer(self, primer_json_data):
        return [json_to_primer(item) for item in primer_json_data]
    def json_to_persona(self, persona_json_data):
        return [json_to_persona(item) for item in persona_json_data]
    def json_to_message_history(self, message_history_json_data):
        return [json_to_message_history(item) for item in message_history_json_data]
    def chain_to_json(self, chain_objects):
        return [chain_to_json(obj) for obj in chain_objects]
    def primer_to_json(self, primer_objects):
        return [primer_to_json(obj) for obj in primer_objects]
    def persona_to_json(self, persona_objects):
        return [persona_to_json(obj) for obj in persona_objects]
    def message_history_to_json(self, message_history_objects):
        return [message_history_to_json(obj) for obj in message_history_objects]