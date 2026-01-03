import streamlit as st
import time
st.title("Simple Addition Calculator")
# st.header("Header")
n1 = st.number_input("Enter first number")
n2 = st.number_input("Enter second number")

if st.button("Add"):
    add = n1 + n2
    st.balloons()
    st.success(f"The sum is {add}")
    
st.write("") 
st.text_area("Long text")

# st.selectbox("Select")