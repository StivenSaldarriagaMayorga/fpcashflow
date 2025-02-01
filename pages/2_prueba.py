import streamlit as st
import pandas as pd

st.sidebar.image("https://5pa.co/5PA/web/images/Logo_5PA2.PNG", use_container_width=True)

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
tab1.subheader("Subtitulo del tab 1")
tab2.subheader("Subtitulo del tab 2")

with tab1:
  with st.popover("Registrar transaccion", use_container_width=True):
    with st.form("formulario1"):
      entry_1 = st.text_input("Dato 1", placeholder="Ingrese el dato...")
      submitted = st.form_submit_button("Aceptar")
      if submitted:
        st.write("Dato ingresado:", entry_1)

with tab2:
  with st.popover("Registrar transaccion"):
    with st.form("formulario2"):
      entry_2 = st.text_input("Dato 2", placeholder="Ingrese el dato...")  
      submitted = st.form_submit_button("Aceptar")
      if submitted:
        st.write("Dato ingresado:", entry_2)

