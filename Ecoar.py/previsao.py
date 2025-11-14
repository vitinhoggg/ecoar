import streamlit as st
import pandas as pd
from modelo import carregar_modelo_e_dados

# 🔥 Nova Função de Alertas Inteligentes
def gerar_alerta(nota, presenca):
    alertas = []

    if presenca <= 66.5:
        alertas.append("⚠️ **Presença muito baixa — alto risco segundo a árvore de decisão.**")

    if nota <= 5.8:
        alertas.append("⚠️ **Notas abaixo do limite crítico detectado na árvore.**")

    if presenca <= 61.5 and nota <= 8.25:
        alertas.append("🚨 **Alerta severo: combinação de baixa presença e nota reconhecida como risco elevado.**")

    if len(alertas) == 0:
        alertas.append("✅ Nenhum indicador crítico encontrado segundo a árvore.")

    return alertas


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

        st.subheader("📢 Sistema de Alertas Baseado na Árvore de Decisão")
        alertas = gerar_alerta(nota, presenca)
        for alerta in alertas:
            st.warning(alerta)

        st.subheader("🎯 Resultado Final")
        if resultado == 1:
            st.error("⚠️ Alto risco de evasão")
        else:
            st.success("✅ Baixo risco de evasão")
