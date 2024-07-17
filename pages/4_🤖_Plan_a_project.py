import streamlit as st
import requests
import json


def center_button(n_element:int):

    js = f'''
    <script>
    // Find all the buttons
    var buttons = window.parent.document.getElementsByClassName("stButton");
    
    // Select one of them
    var button = buttons[{n_element}];
    
    // Modify the color
    button.style.borderRadius = '10px';
    button.style.alignItems = 'center';
    button.style.fontWeight = 'bold';
    button.style.display = 'flex';
    button.style.padding = '10px';
    button.style.justifyContent = 'center';
    button.style.alignItems = 'center';
    button.style.textTransform = 'uppercase';
    </script>
    '''
    st.components.v1.html(js, height=0)

st.set_page_config(
    page_title="Plan a project",
    page_icon="🤖",
)
st.markdown("""
    <style>
    .stTextArea [data-baseweb=base-input] {
        background-image: linear-gradient(140deg, rgb(20, 60, 34) 0%, rgb(160, 28, 57) 50%, rgb(30,30,90) 80%);
        
        -webkit-text-fill-color: #0ef0e8;
    }
    </style>
    """,unsafe_allow_html=True)

st.markdown(
    """
    <style>
    span[data-baseweb="tag"] {
    background-color: slateblue !important;
    font-family: "Baloo Tamma 2", cursive;
    }
    </style>
    """,
        unsafe_allow_html=True,
)

st.markdown(
    """
    <div style='background-color: #f0f0f0; padding: 20px; margin: 30px; border-radius: 10px; '>
    <h3 style='color: #ff69b4; font-style: italic; font-family: Algerian; text-align: center;'>🚀 Welcome to the Project Armory ! 🚀</h3>
    <p style='color:#00bfff; font-size:18px;'>This room is a treasure trove to plan projects. Get help to code projects</p>
    </div>
    """,
    unsafe_allow_html=True
)

conta = st.container(border=True)
with conta:
    project_name = st.text_area("Enter the name of the project", height=25)
    project_description = st.text_area("Enter the description of the project", height=75)
    project_tech = st.multiselect("Choose the technologies and languages you'd like to use in the project",[
        "Python",
        "JavaScript",
        "React",
        "Node.js",
        "Django",
        "Flask",
        "HTML",
        "CSS",
        "Bootstrap",
        "Tailwind CSS",
        "Machine Learning",
        "Data Science",
        "Computer Vision",
        "Natural Language Processing",
        "Angular",
        "Vue.js",
        "Swift",
        "Java",
    ])
    add_tech = st.text_area("Write down any additional technologies or languages you'd like to use in the project (if not in the list above)")
    submit = st.button("Plan the project")
    center_button(0)
if submit:
    data = {
        "model": "codestral-latest",
        "messages": [
            {"role": "user", "content": f"DON'T GIVE THE PLAN. Give the scripts of project: {project_name} with the description: {project_description} using the technologies: {project_tech} and additional technologies: {add_tech}"},
        ]
    }
    headers = {
        "Authorization": f"Bearer {st.secrets['CODESTRAL_KEY']}",
        "Content-Type": "application/json"
    }
    code_ep=str(st.secrets['CODESTRAL_URL'])
    response = requests.post(code_ep, data=json.dumps(data), headers=headers)
    st.markdown(response.json()['choices'][0]['message']['content'])
