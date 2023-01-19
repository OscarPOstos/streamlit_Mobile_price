import streamlit as st
from PIL import Image
import sys

sys.path.insert(0, 'model')

from model.mobile import MobileModel


def set_first_section(mobile):
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
        mobile.set_mAh(mAh)
        gb_intern_memory = st.number_input("Enter intern memory in GB:", step=1)
        mobile.set_intern_memory(gb_intern_memory)
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
        mobile.set_clock_speed(clock_speed)
        ram = st.number_input("Enter ram memory in MB:", step=1000)
        mobile.set_ram(ram)


def set_second_section(mobile):
    columns2 = st.columns(3)
    with columns2[0]:
        primary_camera = st.number_input("Enter the mega px of the primary camera:", step=1.0)
        mobile.set_primary_camera(primary_camera)
        dual_sim = st.checkbox('Dual sim?')
        mobile.set_dual_sim(dual_sim)
    with columns2[1]:
        image = Image.open('static/images/mobile.png')
        st.text("")
        st.text("")
        st.text("")
        st.image(image, width=200)
        width = st.number_input("Enter the width in px of the mobile", step=1.0)
        mobile.set_width(width)
    with columns2[2]:
        frontal_camera = st.number_input("Enter the mega px of the frontal camera:", step=1.0)
        mobile.set_frontal_camera(frontal_camera)
        height = st.number_input("Enter the height in px of the mobile", step=1.0)
        mobile.set_height(height)
