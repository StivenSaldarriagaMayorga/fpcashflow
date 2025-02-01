import streamlit as st
import pandas as pd
from uuid import uuid4
from utils.store import work as w, transaction_movement as ts


@st.dialog("Registrar nueva obra")
def register_work():
  name = st.text_input("Nombre:")
  payment = st.number_input('Pago Estipulado:')
  start = st.date_input("Fecha de comienzo:")
  end = st.date_input("Fecha de finalización:")
  if st.button("Registrar"):
    id = str(uuid4())
    w.loc[id] = [name, payment, pd.to_datetime(start), pd.to_datetime(end)]
    st.rerun()


@st.dialog("Registrar nueva transacción")
def register_transaction():
#   no_invoice = st.text_input('Número de factura:')
  description = st.text_input("Asunto:")
  work_id = st.selectbox('Obra relacionada:', ["Obra1", "Obra 2"])
  mov_type = st.selectbox('Obra relacionada:', ["Gasto", "Ingreso"])
  subject = st.text_input('Destinatario:' if mov_type == 'Gasto' else 'Origen')
  category = st.selectbox("Categoría:", ["Periódico", "Único"])
  amount = st.number_input("Monto total:", step=10000)
  date_transaction = st.date_input("Fecha de transacción:")
  end_transaction = pd.NaT
  last_transaction = pd.NaT
  if category == "Periódico":
    last_transaction = st.date_input("Fecha del pago previo:")
    end_transaction = st.date_input("Fecha de finalización:")
  stabilization_fund_percentage = 0
  if mov_type == 'Ingreso':
    st.write("Metale all-in al rojo")
    stabilization_fund_percentage = st.slider('Porcentaje destinado a fondo de estabilización', 0, 100, 5)
  if st.button("Registrar"):
    id = str(uuid4())
    ts.loc[id] = [
        work_id,
        description,
        'one_time' if category == 'Único' else 'monthly',
        pd.to_datetime(date_transaction),
        pd.to_datetime(end_transaction),
        pd.to_datetime(last_transaction),
        'exprense' if mov_type == 'Gasto' else 'income',
        amount,
        stabilization_fund_percentage,
        subject
        ]
    st.rerun()
