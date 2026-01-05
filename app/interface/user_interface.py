import streamlit as st

def clear_input():
    st.session_state['user_input'] = ''

def run_app():
    st.title('NLP Project')
    st.text_area('Text:', key='user_input', placeholder='Enter your text...')
    st.button('Summarize')
    st.button('Clear', on_click=clear_input)