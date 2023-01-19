import streamlit as st
import joblib
import pandas as pd
from model.mobile import MobileModel
from components.components import *
from static.style.style import set_style

mobile = MobileModel(0, 0, False, 0, 0, 0, 0, 0, 0)

set_style()

st.title("Streamlit Mobile price ML")

set_first_section(mobile)
set_second_section(mobile)

submit = st.button("Submit")

if submit:
    mobile_model = joblib.load(open('model/mobile_model.pkl', 'rb'))
    X = pd.DataFrame([[mobile.mAh, mobile.clock_speed, mobile.dual_sim, mobile.frontal_camera,
                       mobile.gb_intern_memory, mobile.primary_camera, mobile.height, mobile.width, mobile.ram]],
                     columns=["battery_power", "clock_speed", "dual_sim",
                              "fc", "int_memory", "pc", "px_height", "px_width", "ram"])
    X = X.replace([True, False], [1, 0])
    prediction = mobile_model.predict(X)[0]
    st.text(f"{20 + int(prediction) * 120}$ aproximadamente")
