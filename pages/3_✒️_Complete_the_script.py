import streamlit as st
import requests
import json
from io import StringIO


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
    page_title="Complete the script",
    page_icon="✒️",
)
st.markdown("""
    <style>
    .stTextArea [data-baseweb=base-input] {
        background-image: linear-gradient(140deg, rgb(245, 185, 44) 0%, rgb(51, 23, 18) 50%, rgb(48, 74, 55) 80%);
        
        -webkit-text-fill-color: #0ef0e8;
    }
    </style>
    """,unsafe_allow_html=True)

st.markdown(
    """
    <div style="background-color: #f9f9f9; padding: 20px; margin: 30px; border-radius: 10px;">
    <h3 style='text-align: center; color:#ff69b4 ;font-style:italic; font-family:Algerian'>🚀Welcome to Helper Room! 🚀</h3>
    <p style="font-size: 18px; color:#00bfff">This room magically completes your incomplete scripts in a chiffy.</p>
    <p style="font-size: 12px; color:#00bfff">Use either text area or the file uploader to input the script.</p>

    </div>
    """,
    unsafe_allow_html=True
)

con=st.container(border=True)
with con:
    left,mid,right= st.columns(3)
    with left:
        script=st.text_area("Enter your script here",height=200,key="code",)
    with mid:
        st.markdown("<h6 style='text-align: center; color:slateblue ;font-style:italic; font-family:Algerian'>OR</h6>", unsafe_allow_html=True)
    with right:
        file_script=st.file_uploader("Upload your script here")
        if file_script:
            string_io=StringIO(file_script.getvalue().decode("utf-8"))
            script=string_io.read()
    lang=st.selectbox("Select the coding language", ["Python", "Java", "C++", "JavaScript", "Ruby", "Go","Bash", "Rust", "TypeScript", "Swift", "Kotlin", "PHP", "R", "Scala", "Perl", "Haskell","Julia", "Elixir", "Clojure","Lua"])
    color_selectbox(0,"#0ef0e8")
    constr=st.text_area("Write down the question or extra information (if any)",height=100)

    submit=st.button("Complete it")
    center_button(0)

if submit:
    data = {
        "model": "codestral-latest",
        "messages": [
            {"role": "user", "content": f"Complete this script to the fullest: {script} in {lang} language, while following the constraints {constr}"},
        ]
    }
    headers = {
        "Authorization": f"Bearer {st.secrets['CODESTRAL_KEY']}",
        "Content-Type": "application/json"
    }
    code_ep=str(st.secrets['CODESTRAL_URL'])
    response = requests.post(code_ep, data=json.dumps(data), headers=headers)
    st.markdown(response.json()['choices'][0]['message']['content'])