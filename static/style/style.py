import streamlit as st


def set_style():
    st.text("prueba")
    st.markdown("""<style>
                section.main.css-k1vhr4.egzxvld5 {
                    background-image: url("https://static.vecteezy.com/system/resources/previews/004/631/777/non_2x/black-triangular-modern-background-free-vector.jpg");
                    background-size: cover;
                }
                
                .block-container.css-91z34k.egzxvld4 {
                    background-color: #ffffff4a;
                    border-radius: 20px
                }
                </style>""", unsafe_allow_html=True)
