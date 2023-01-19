import streamlit as st


def set_style():
    st.text("prueba")
    st.markdown("""<style>
                .main css-k1vhr4 egzxvld5 {
                background-image: url('static/images/background.gif')
                }
                </style>""", unsafe_allow_html=True)
