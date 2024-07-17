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
    page_title="Get a question",
    page_icon="🧑‍💻",
)

st.markdown(
    """
    <div style="background-color: #f9f9f9; padding: 20px; margin: 30px; border-radius: 10px;">
        <h3 style="color: #ff69b4; font-style:italic; font-family:Algerian">🚀 Welcome to Testing Room! 🚀</h3>
        <p style="font-size: 18px; color:#00bfff">I will test your coding skills with an amazing coding question.</p>
        <p style="font-size: 18px; color:#00bfff">Choose your preferred settings and get ready to solve the question.</p>
    </div>
    """,
    unsafe_allow_html=True
)
cont = st.container(border=True)
with cont:
    difficulty  = st.selectbox("Select the difficulty level",
        ["Easy", "Medium", "Hard"])
    color_selectbox(0, "slateblue")

    dsa = st.selectbox("Select the DSA topic you'd like to test",
        ["Your Choice Majesty","Arrays", "Strings", "Linked Lists", "Stacks", "Queues", "Trees", "Graphs", "Dynamic Programming", "Backtracking", "Greedy Algorithms", "Bit Manipulation", "Hashing", "Searching and Sorting", "Recursion", "Tries", "Heaps", "Math"])
    color_selectbox(1, "burlywood")

    submit= st.button("Get a question")
    center_button(0)

if submit:
    data = {
        "model": "codestral-latest",
        "messages": [
            {"role": "user", "content": f"DON'T REPEAT QUESTIONS, GIVE DIFFERENT QUESTION EVERYTIME. Give me a {difficulty} coding question in the topic {dsa}. Don't give me the answer, I want to solve it myself. Add test cases if possible."}
        ]
    }
    headers = {
        "Authorization": f"Bearer {st.secrets['CODESTRAL_KEY']}",
        "Content-Type": "application/json"
        }
    code_ep=str(st.secrets['CODESTRAL_URL'])
    response = requests.post(code_ep, data=json.dumps(data), headers=headers)
    st.markdown(response.json()['choices'][0]['message']['content'])
