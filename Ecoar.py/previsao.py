import streamlit as st
import pandas as pd
from modelo import carregar_modelo_e_dados

def mostrar_previsao():
    st.title("🎯 Previsão de Evasão Acadêmica")
    modelo, df = carregar_modelo_e_dados()

    idade = st.number_input("Idade", min_value=15, max_value=80, value=20)
    nota = st.slider("Média das notas", min_value=0.0, max_value=10.0, value=7.5)
    presenca = st.slider("Percentual de presença", min_value=0, max_value=100, value=80)

    entrada = pd.DataFrame({
        "idade": [idade],
        "nota": [nota],
        "percentual_presenca": [presenca]
    })

    if st.button("Prever"):
        resultado = modelo.predict(entrada)[0]
        if resultado == 1:
            st.error("⚠️ Alto risco de evasão")
        else:
            st.success("✅ Baixo risco de evasão")