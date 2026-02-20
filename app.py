import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt  

st.title ('ML model demo')
st.header('Prediction system')
st.subheader('Enter inputs Below')
st.write('this app demonstrate ML model deployment')
name = st.text_input("Enter customer name")
age = st.number_input("Enter Age:", min_value=0, max_value=100)
salary = st.slider("Select Salary", 10000, 100000)
gender = st.selectbox("Select Gender", ["male", "female"])
education = st.radio("Educational level", ["UG", "PG", "PhD"])
agree = st.checkbox("I agree to terms")
upload_file = st.file_uploader("upload image", type=["jpg", "png"])
if st.button("predict"):
    st.success("prediction  successful")
    st.warning("warning")
    st.error("error, enter a valid input")
df = pd.DataFrame({"A":[1,2], "B":[3,4]})
st.dataframe(df)

appointment = st.date_input("Select the appointment date")
st.write("Appointment date:", appointment)
time = st.time_input("Select appointment time")
st.write("Appointment time:", time)
#To display result
st.metric("Accuracy", "92%", "+2%")
#image display
#image = Image.open("mango.webp")
st.image("Nature.jpeg")
#st.audio("<audio file name>")
#st.video("<video file name>")
#Sidebar - for Multipage apps
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose page",["Home", "Predictions"])

#layout control
col1,clo2 = st.columns(2)
with col1:
    st.write("Left")
with clo2:
    st.write("right")

#progress & spinners (ML/DL Models)
with st.spinner("processing"):
    #result = model.predict(data)
    st.progress(50)

#Caching Model (very imp)
# Prevents reloading model everytime
#@st.cache_resourse

#def load_model():
 #   return joblib.load("model.pkl")

#model = load_model()

data = {
    'Name': ['Divya', 'Sri', 'anna' , 'peter'],
    'age': [19,20,21,22],
    'City': ['India', 'Europe', 'Paris', 'London']
}
df = pd.DataFrame(data)
st.dataframe(df)

#display some charts
rand = np.random.normal(1,2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)