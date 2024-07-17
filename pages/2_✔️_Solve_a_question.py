import streamlit as st
import requests
import json

def color_selectbox(n_element:int, color:str):

    js = f'''
    <script>
    // Find all the selectboxes
    var selectboxes = window.parent.document.getElementsByClassName("stSelectbox");
    
    // Select one of them
    var selectbox = selectboxes[{n_element}];
    
    // Select only the selection div
    var selectregion = selectbox.querySelector('[data-baseweb="select"]');
    
    // Modify the color
    selectregion.style.backgroundColor = '{color}';
    selectregion.style.border = '4px solid {color}';
    selectregion.style.borderRadius = '10px';
    selectregion.style.alignItems = 'center';
    selectregion.style.fontWeight = 'bold';
    </script>
    '''
    st.components.v1.html(js, height=0)


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
    page_title="Solve a question",
    page_icon="✔️",
)
st.markdown("""
    <style>
    .stTextArea [data-baseweb=base-input] {
        background-image: linear-gradient(140deg, rgb(54, 36, 31) 0%, rgb(121, 56, 100) 50%, rgb(106, 117, 25) 80%);
        
        -webkit-text-fill-color: #0ef0e8;
    }
    </style>
    """,unsafe_allow_html=True)

st.markdown(
    """
    <div style="background-color: #f9f9f9; padding: 20px; margin: 30px; border-radius: 10px;">
    <h3 style='text-align: center; color:#ff69b4 ;font-style:italic; font-family:Algerian'>🚀Welcome to Solutions Room! 🚀</h3>
    <p style="font-size: 18px; color:#00bfff">This room provides solution to all your coding question</p>
    </div>
    """,
    unsafe_allow_html=True
)


conter=st.container(border=True)
with conter:
    question=st.text_area("Enter your question here",height=150)
    lang=st.selectbox("Select the coding language", ["Python", "Java", "C++", "JavaScript", "Ruby", "Go","Bash", "Rust", "TypeScript", "Swift", "Kotlin", "PHP", "R", "Scala", "Perl", "Haskell","Julia", "Elixir", "Clojure","Lua"])
    color_selectbox(0,"#0ef0e8")
    constr=st.text_area("Write down constraints (if any)",height=100)

    submit=st.button("Solve it")
    center_button(0)

if submit:
    data = {
        "model": "codestral-latest",
        "messages": [
            {"role": "user", "content": f"Solve this coding question: {question} in {lang} language, while following the constraints {constr}"},
        ]
    }
    headers = {
        "Authorization": f"Bearer {st.secrets['CODESTRAL_KEY']}",
        "Content-Type": "application/json"
    }
    code_ep=str(st.secrets['CODESTRAL_URL'])
    response = requests.post(code_ep, data=json.dumps(data), headers=headers)
    st.markdown(response.json()['choices'][0]['message']['content'])