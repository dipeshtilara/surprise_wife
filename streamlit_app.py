import streamlit as st
import streamlit.components.v1 as components

# Set page config to use full screen layout
st.set_page_config(layout="wide", page_title="For My Love", page_icon="❤️")

# Hide Streamlit specific elements to make it look like a standalone site
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {padding-top: 0rem; padding-bottom: 0rem; padding-left: 0rem; padding-right: 0rem;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Read the HTML file
try:
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Render the HTML
    # height=800 is a safe default, scrolling is enabled if needed
    components.html(html_content, height=800, scrolling=False)

except FileNotFoundError:
    st.error("Could not find index.html. Please ensure it is in the same directory.")
