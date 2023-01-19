import streamlit as st
# import joblib
# import pandas as pd
from PIL import Image

image = Image.open('static/images/bateria.png')

st.title("Streamlit Mobile price ML")

# Add a text input
st.image()
height = st.number_input("Enter the battery power in mAh:", step=1.0)
submit = st.button("Submit")

# Display the entered name
if submit:
    pass
    # pickled_model = joblib.load(open('model/mobile_model.pkl', 'rb'))
    # X = pd.DataFrame([[height, weight, color_eyes]], columns=["Height", "Weight", "Eye"])
    # X = X.replace(["Brown", "Blue"], [1, 0])
    # prediction = pickled_model.predict(X)[0]
    # st.text(prediction)
