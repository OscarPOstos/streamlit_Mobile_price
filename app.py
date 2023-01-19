import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st
import joblib
import pandas as pd
from PIL import Image

image = Image.open('sus.gif')

st.title("Streamlit Machine Learning App")

# Add a text input
st.image(image, caption='among us')
height = st.number_input("Enter your Height:", step=1.0)
weight = st.number_input("Enter your Weight:", step=1.0)
color_eyes = st.selectbox("Enter your color eyes:", ('Brown', 'Blue'))
submit = st.button("Submit")

# Display the entered name
if submit:
    pickled_model = joblib.load(open('pet_model.pkl', 'rb'))
    X = pd.DataFrame([[height, weight, color_eyes]], columns=["Height", "Weight", "Eye"])
    X = X.replace(["Brown", "Blue"], [1, 0])
    prediction = pickled_model.predict(X)[0]
    st.text(prediction)
