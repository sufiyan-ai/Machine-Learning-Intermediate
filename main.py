import streamlit as st
import joblib
import numpy as np
import os

if os.path.exists('model.pkl'):
    model = joblib.load('model.pkl')
else:
    st.error("Model file not found. Please upload 'model.pkl'.")

st.title('Fraud Detection System')


inp1 = int(st.number_input("Enter the Type of Transaction: CASH_OUT: 1, PAYMENT: 2, CASH_IN: 3, TRANSFER: 4, DEBIT: 5 (integer): ",value=0))
inp2 = float(st.number_input("Enter the Amount of Transaction (float): ",value=0))
inp3 = float(st.number_input("Enter the Balance Amount of Origin's Old Balance (float): ",value=0))
inp4 = float(st.number_input("Enter the Balance Amount of Origin's New Balance (float): ",value=0))
inp5 = float(st.number_input("Enter the Balance Amount of Destination's Old Balance (float): ",value=0))
inp6 = float(st.number_input("Enter the Balance Amount of Destination's New Balance (float): ",value=0))


if st.button("Predict"):
    inp = np.array([[inp1, inp2, inp3, inp4, inp5, inp6]])
    
    #result = model.predict(inp)
    
    st.success(f"This Transaction is: {model.predict(inp)}")
