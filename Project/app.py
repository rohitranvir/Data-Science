import streamlit as st
import pandas as pd
import pickle
import numpy as np
# with open("obesity_model.pkl","rb") as file:
#     model=pickle.load(file)
loded_model=pickle.load(open("obesity_model.pkl",'rb'))
def prediction(input_data):
    input_data=[float(x) for x in input_data]
    input_data_as_arr=np.asarray(input_data)
    input_data_reshaped=input_data_as_arr.reshape(1,-1)
    input_data_reshaped = scaler.transform(input_data_reshaped)
    prediction=loded_model.predict(input_data_reshaped)
    if prediction == 0 :
        return "Insufficient Weight"
    elif prediction == 1 :
        return "Normal Weight"
    elif prediction == 2 :
        return "Overweight Level I"
    elif prediction == 3 :
        return "Overweight Level II"
    elif prediction == 4 :
        return "Obesity Type I"
    elif prediction == 5 :
        return "Obesity Type II"
    elif prediction == 6 :
        return "Obesity Type III"
    else:
        return "Problems In your code"
    


def main():
    st.title("Obasity checking")
    Screen_time= st.text_input("Enter your Screen Time")
    Weight= st.text_input("Enter you weight")
    consumption_of_vegetables=st.text_input("Enter consumption_of_vegetables")
    Age= st.text_input("Enter your Age")
    Height= st.text_input("Enter your Height")
    Gender= st.selectbox("Gender",["Male", "Female"])
    dignosis=''
    Gender=1 if Gender=='Male' else 0
    if st.button("Check obasity"):
        dignosis=prediction([Screen_time,Weight,consumption_of_vegetables,Age,Height,Gender])
    st.success(dignosis)
if __name__=='__main__':
    main()