import streamlit as st
import pandas as pd
from utils.auth0 import getAuth0
import base64
from utils.store import transaction_movement as tm

st.sidebar.image("https://5pa.co/5PA/web/images/Logo_5PA2.PNG", use_container_width=True)

user_info = getAuth0()
if user_info:
    st.write("### Cash Flow")
    col1, col2, col3 = st.columns(3)
    income = tm[tm['transaction_type'] == 'income']['amount'].sum()
    expense = tm[tm['transaction_type'] == 'expense']['amount'].sum()
    balance = income - expense
    col1.metric(label="Ingresos", value=f"${income:,.0f}")
    col2.metric(label="Balance", value=f"${balance:,.0f}")
    col3.metric(label="Egresos", value=f"${expense:,.0f}")