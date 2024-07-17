import streamlit as st

st.set_page_config(
    page_title="King Coder",
    page_icon="👑",
)

st.title(":rainbow[Hi, there!!! Welcome to the court of majestic ***King Coder***] 👑")

st.markdown(
    """
    <div style="background-color: #f9f9f9; padding: 20px; border-radius: 10px; font-family: Arial, sans-serif;">
        <h3 style="color: #ff69b4; font-size: 24px; font-style: italic">King Coder is here to help you with your coding journey.</h3>
        <p style="font-size: 18px; color: #00bfff; font-style: italic">I can help you with the following:</p>
        <ol style="font-size: 14px; color: #00bfff;">
            <li>Test you with an amazing coding question</li>
            <li>Solve your coding problems in any language</li>
            <li>Complete your incomplete scripts</li>
            <li>Plan a project for you</li>
            <li>Translate your code to any language</li>
            <li>Explain any script you have</li>
        </ol>
        <p style="font-size: 16px; color: #ff69b4;">Choose the task you want me to do from the sidebar on the left.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <div style="border: 3px solid; border-image: linear-gradient(to right, #13547a, #80d0c7); border-image-slice: 1; padding: 10px; border-radius: 20px; font-family: Arial, sans-serif; text-align: center;">
        <h3 style="color: #ff69b4; font-size: 18px; font-style: italic">Choose a task from above</h3>
    </div>
    """,
    unsafe_allow_html=True
)
