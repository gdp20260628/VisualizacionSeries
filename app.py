import streamlit as st

st.title("Grafica de serie de tiempo")

entrada = st.text_input("Ingrese la serie, separada por comas:",value="10,15,18,26,31")
entrada2 = entrada.split(",")

serie = [float(i) for i in entrada2]

st.line_chart(serie)
