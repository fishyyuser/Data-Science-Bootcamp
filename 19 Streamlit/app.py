import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Streamlit")

st.write("This is a simple text")

df=pd.DataFrame({
    'first coloumn':[1,2,3,4,5],
    'second coloumn':[100,20,30,43,54]
})
st.write(df)

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)
