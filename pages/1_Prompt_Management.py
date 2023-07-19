import streamlit as st
import json

st.title("Prompt Management")

def open_json_file(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        if not data:
            return []
        return data

def create_dict(path, title):
  
    prompts = open_json_file(path)    
    if prompts ==[]:
        return
    return {prompt[title]: prompt for prompt in prompts}

prompts_path = "src/static/prompts/prompts.json"
prompt_title = "message"
prompts = open_json_file(file_path=prompts_path)
prompt_dict = create_dict(path=prompts_path, title=prompt_title)
chain_path = "src/static/prompt_chains/chains.json"
chain_title = "Chain Title"
chains = open_json_file(file_path=chain_path)
chain_dict = create_dict(path=chain_path, title=chain_title)
persona_path = "src/static/personas/personas.json"
persona_title = "Persona Title"
personas = open_json_file(file_path=persona_path)
persona_dict = create_dict(path=persona_path, title=persona_title)
primers_path = "src/static/primers/primers.json"
primers_title = "Primers Title"
primers = open_json_file(file_path=primers_path)
primers_dict = create_dict(path=primers_path, title=primers_title)

temp_chain = []
def save_json_file(path, title, new_title):
    temp_chain.append(json.dumps({title: f'{new_title}'}))
    for  option in options:
        temp_chain.append(json.dumps(prompt_dict[option]))
    with open (path, "r") as f:
        chains = json.loads(f.read())    
        chains.append(temp_chain)
    with open (path, "w") as f:
        f.write(chains)

sidebar = st.sidebar
sidebar.header('Prompts')
with sidebar:
    options = st.multiselect(options=list(prompt_dict.keys()), label="Select prompts")
    new_chain_title = st.text_input("Enter title to save chain")
    st.button("Save chain", on_click=save_json_file(path=chain_path, title=chain_title, new_title=new_chain_title))

content = []
for option in options:    
    chain = st.subheader(f"{prompt_dict[option]['message']['role']}:{prompt_dict[option]['message']['content']}")

    sidebar.header('Personas')
    
    selected_persona_title = sidebar.selectbox('Choose a persona', options=list(persona_dict.keys()))

    selected_persona = persona_dict[selected_persona_title]

    sidebar.image(selected_persona['image'], width=200)

    st.markdown(selected_persona['description'])

st.header('Create a new prompt')
new_prompt_title = st.text_input('Enter prompt title')
new_prompt_role = st.text_input('Enter role')
new_prompt_content = st.text_input('Enter content')

if st.button('Save new prompt'):
    new_prompt = {"message":{"role":new_prompt_role, "content": new_prompt_content},"title":new_prompt_title}
    prompts.append(new_prompt)
    prompt_dict[new_prompt_title] = new_prompt
    st.success('Saved new prompt')
