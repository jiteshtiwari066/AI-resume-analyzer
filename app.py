import streamlit as st
import ollama

st.title("AI Resume Analyzer 🚀")

resume = st.text_area("Apna Resume Paste karo:")

if st.button("Analyze Resume"):
    if resume:
        st.write("Analyzing...")

        prompt = f"""
        You are a professional resume reviewer.

        Analyze the resume and give:

        Strengths
        Weaknesses
        Missing Skills
        Suggestions
        Score out of 100

        Resume:
        {resume}
        """

        
        response = ollama.chat(
    model='llama3',
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

output = ""

for chunk in response:
    output += chunk['message']['content']
    st.write(output)