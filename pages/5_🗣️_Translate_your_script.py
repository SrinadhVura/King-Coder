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
    page_title="Translate your script",
    page_icon="🗣️",
)

st.markdown("""
    <style>
    .stTextArea [data-baseweb=base-input] {
        background-image: linear-gradient(140deg, rgb(49, 19, 56) 0%, rgb(179, 85, 34) 50%, rgb(198, 204, 12) 80%);
        
        -webkit-text-fill-color: #0ef0e8;
    }
    </style>
    """,unsafe_allow_html=True)

st.markdown(
    """
    <div style="background-color: #f9f9f9; padding: 20px; margin: 30px; border-radius: 10px;">
    <h3 style='text-align: center; color:#ff69b4 ;font-style:italic; font-family:Algerian'>🚀Welcome to Translator's room!🚀</h3>
    <p style="font-size: 18px; color:#00bfff">I am a linguist. I know all the programming languages and can translate your script easily.</p>
    </div>
    """,
    unsafe_allow_html=True
)

co = st.container(border=True)
with co:

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
    langs=["Python", "Java", "C++", "JavaScript", "Ruby", "Go","Bash", "Rust", "TypeScript", "Swift", "Kotlin", "PHP", "R", "Scala", "Perl", "Haskell","Julia", "Elixir", "Clojure","Lua"]
    left, right = st.columns(2)
    with left:
        lang=st.selectbox("Select the language of the script you entered above",langs,placeholder="Source language")
        color_selectbox(0,"tomato")
    
    with right:
        lang2=st.selectbox("Select the language to translate to",langs,placeholder="Destination language")
        color_selectbox(1,"chartreuse")
    submit=st.button("Translate it")
    center_button(0)

if submit:
    if lang==lang2:
        st.error("Source and destination languages cannot be same. Please select different languages.")
        st.stop()
    data = {
        "model": "codestral-latest",
        "messages": [
            {"role": "user", "content": f"Translate the following script: {script} in {lang} language, to {lang2} language"},
        ]
    }
    headers = {
        "Authorization": f"Bearer {st.secrets['CODESTRAL_KEY']}",
        "Content-Type": "application/json"
    }
    code_ep=str(st.secrets['CODESTRAL_URL'])
    response = requests.post(code_ep, data=json.dumps(data), headers=headers)
    st.markdown(response.json()['choices'][0]['message']['content'])