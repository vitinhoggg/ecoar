import streamlit as st
from dashboard import mostrar_dashboard
from previsao import mostrar_previsao

st.set_page_config(page_title="ECOAR", page_icon="🎓")

st.title("🎓 ECOAR — Sistema de Previsão de Evasão Acadêmica")

st.sidebar.title("Menu")
pagina = st.sidebar.radio("Navegar para:", ["Dashboard", "Previsão", "Sobre"])

if pagina == "Dashboard":
    mostrar_dashboard()
elif pagina == "Previsão":
    mostrar_previsao()
else:
    st.write("""
    ### ℹ️ Sobre o ECOAR

    Projeto acadêmico para prever risco de evasão estudantil usando Machine Learning.

    **Tecnologias:**
    - Python
    - Streamlit
    - MySQL
    - Scikit-learn
    - Matplotlib & Seaborn
    """)