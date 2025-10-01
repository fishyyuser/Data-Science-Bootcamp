import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")
name=st.text_input("Enter your name")
age=st.slider('Select your age',3,120,25)

if name:
    st.write(f'Hello {name}')
    
st.write(f'You are {age} years old')

options=['Python','Java','C++','JavaScript']
choice=st.selectbox('Choose your favourite language:',options)
st.write(f'Your favourite language is {choice}')

# df=pd.DataFrame({
#     'Name':['Jack Jack','Elastic Girl','Dash','Syndrome'],
#     'Gender':['Male','Female','Male','Male']
# })

# st.write(df)
uploaded_file=st.file_uploader("Choose a CSV file",type='csv')

if uploaded_file:
    df=pd.read_csv(uploaded_file)
    st.write(df)