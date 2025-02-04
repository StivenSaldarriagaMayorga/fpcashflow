import streamlit as st
import pandas as pd
from utils.auth0 import getAuth0
import base64
from utils.store import transaction_movement as tm

st.sidebar.image("https://5pa.co/5PA/web/images/Logo_5PA2.PNG", use_container_width=True)

user_info = getAuth0()
if user_info:
    st.write("### Cash Flow")
    col1, col2, col3, col4 = st.columns(4)
    income = tm[tm['transaction_type'] == 'income']['amount'].sum()
    expense = tm[tm['transaction_type'] == 'expense']['amount'].sum()
    balance = income - expense
    col1.metric(label="Ingresos", value=f"${income:,.0f}")
    col2.metric(label="Balance", value=f"${balance:,.0f}")
    col3.metric(label="Egresos", value=f"${expense:,.0f}")

    sum_income=(1/100)*(tm[tm['transaction_type'] == 'income']['amount']* tm[tm['transaction_type'] == 'income']['stabilization_fund_percentage']).sum()
    sum_expense=(1/100)*(tm[tm['transaction_type'] == 'expense']['amount']* tm[tm['transaction_type'] == 'expense']['stabilization_fund_percentage']).sum()
    
    balance_fund=sum_income-sum_expense
    col4.metric(label="Balance fondo", value=f"${balance_fund:,.0f}")

    with st.container(border=True):
        tm_incomes = tm.copy(True)
        tm_incomes = pd.DataFrame(tm_incomes[tm_incomes["transaction_type"] == "income"][["amount", "description", "date"]])
        tm_incomes.rename(columns={"amount":"Ingreso"}, inplace=True)

        st.write("#### Gráfica de ingresos y egresos")
        tm_expenses = tm.copy(True)
        tm_expenses = pd.DataFrame(tm_expenses[tm_expenses["transaction_type"] == "expense"][["amount", "description", "date"]])
        tm_expenses.rename(columns={"amount":"Gasto"}, inplace=True)
        tm_movements_date = pd.merge(tm_incomes[['Ingreso', 'date']], tm_expenses[['Gasto', 'date']], how="outer", on='date')
        
        st.bar_chart(tm_movements_date, y=["Ingreso", "Gasto"], x="date", x_label="Fecha", y_label="Valor")