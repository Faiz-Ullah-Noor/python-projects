import streamlit as st
import pandas as pd

st.title("BMI Calculator")

hight = st.slider("Enter your hight in cm: ", 100, 200, 175)
weght = st.slider("Enter your weight in kg: ", 40, 150, 70)

bmi = weght / ((hight/100) ** 2)
st.header(f"Your BMI is {bmi:.2f}")

st.write("### BMI Categories ###")
st.write("- Underweight BMI: Less than 18.5 ")
st.write("- Normal BMI: Between 18.5 to 24.9 ")
st.write("- OverWeight BMI : 25 to 29.9 ")
st.write("- Obesity: 30 or greater ")