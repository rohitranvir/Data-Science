import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
api_key=os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("API key not found. Please set the GROQ_API_KEY environment variable.")
    st.stop()
client=Groq(api_key=api_key)
st.title("Groq Ai")
question=st.text_input("Ask me anything")
if st.button("Ask"):
    if question=="":
        st.warning("please enter something")
    else:
        try:
            response=client.chat.completions.create(
                model="llama-3.1-8b-instant",
            
                messages=[
                    {"role":"user","content":question}
                ]
            )
            answer=response.choices[0].message.content
            st.write(answer)
        except Exception as e:
            st.error(f"An error occurred: {e}")