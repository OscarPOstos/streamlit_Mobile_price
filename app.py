import streamlit as st
import joblib
# import pandas as pd
from PIL import Image

st.title("Streamlit Mobile price ML")

# Add a text input
columns = st.columns(4)
with columns[0]:
    st.text("")
    st.text("")
    image = Image.open('static/images/bateria.png')
    st.image(image, width=50)
    st.text("")
    st.text("")
    image = Image.open('static/images/memoria_interna.png')
    st.image(image, width=50)
with columns[1]:
    mAh = st.number_input("Enter the battery power in mAh:", step=100)
    gb_intern_memory = st.number_input("Enter intern memory in GB:", step=1)
with columns[2]:
    st.text("")
    st.text("")
    image = Image.open('static/images/procesador.png')
    st.image(image, width=50)
    st.text("")
    st.text("")
    image = Image.open('static/images/memoria_ram.png')
    st.image(image, width=50)
with columns[3]:
    clock_speed = st.number_input("Enter the clock speed:", step=1.0)
    ram = st.number_input("Enter ram memory in MB:", step=1000)
columns2 = st.columns(3)
with columns2[0]:
    primary_camera = st.number_input("Enter the mega px of the primary camera:", step=1.0)
with columns2[1]:
    image = Image.open('static/images/mobile.png')
    st.text("")
    st.text("")
    st.text("")
    st.image(image, width= 200)
    width = st.number_input("Enter the width in px of the mobile", step=1.0)
with columns2[2]:
    frontal_camera = st.number_input("Enter the mega px of the frontal camera:", step=1.0)
    height = st.number_input("Enter the height in px of the mobile", step=1.0)

submit = st.button("Submit")

# Display the entered name
if submit:
    pickled_model = joblib.load(open('model/mobile_model.pkl', 'rb'))
    # X = pd.DataFrame([[height, weight, color_eyes]], columns=["Height", "Weight", "Eye"])
    # X = X.replace(["Brown", "Blue"], [1, 0])
    # prediction = pickled_model.predict(X)[0]
    # st.text(prediction)
