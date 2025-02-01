import streamlit as st
from utils.store import transaction_movement as ts
from utils.auth0 import getAuth0
from ui.modals import register_transaction
st.sidebar.image("https://5pa.co/5PA/web/images/Logo_5PA2.PNG", use_container_width=True)

if getAuth0():

  st.markdown('<h1 style="text-align: center">Transacciones</h1>', unsafe_allow_html=True)

  st.write(ts)
  if st.button('Registrar transacción'):
    register_transaction()
