import streamlit as st
from langchain_groq import ChatGroq

llm = ChatGroq(model="mixtral-8x7b-32768", 
              temperature=0, 
              groq_api_key="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")

def prompt_code(text):
    prompt = f"""
    First you have to detect the language of the code given as input.
    You are a bug detector that detects bugs present in the inputted code and then recommends solutions to fix them.
    The code containing the bug is as follows: {text}
    Generate all the bugs and recommend optimized solutions.
    """
    response = llm.invoke(prompt)
    return response.content


st.title("Code Bug Detector")
st.write("Enter your code below, and the AI will detect bugs and suggest fixes.")

user_input = st.text_area("Paste your code here:", height=200)

if st.button("Detect Bugs"):
    if user_input.strip():
        with st.spinner("Analyzing your code..."):
            result = prompt_code(user_input)
        st.subheader("Bug Report & Fixes:")
        st.write(result)
    else:
        st.warning("Please enter some code before clicking the button.")
