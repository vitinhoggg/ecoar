import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from modelo import carregar_modelo_e_dados, gerar_figura_arvore

sns.set_theme(style="whitegrid", rc={"figure.dpi": 100})

def mostrar_dashboard():
    st.markdown("### 📈 Visão Geral dos Dados Acadêmicos")
    st.write("Explore abaixo as distribuições e correlações entre as variáveis que influenciam o risco de evasão estudantil.")

    modelo, df = carregar_modelo_e_dados()

    st.markdown("<br>", unsafe_allow_html=True)

    left, center, right = st.columns([0.08, 0.84, 0.08])

    with center:
        st.markdown("#### 📊 Distribuições")
        gcol1, gcol2 = st.columns(2, gap="large")

        # Distribuição das Notas
        with gcol1:
            st.markdown("**📘 Distribuição das Notas**")
            fig, ax = plt.subplots(figsize=(6, 3.5))
            sns.histplot(df["nota"], kde=True, ax=ax, color="#1f77b4")
            fig.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)

        # Distribuição da Presença
        with gcol2:
            st.markdown("**🟠 Distribuição da Presença (%)**")
            fig, ax = plt.subplots(figsize=(6, 3.5))
            sns.histplot(df["percentual_presenca"], kde=True, ax=ax, color="#ff7f0e")
            fig.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)

        st.markdown("---")

        st.markdown("#### 🔗 Correlação entre Variáveis")
        fig, ax = plt.subplots(figsize=(8, 4))
        corr = df[["idade", "nota", "percentual_presenca", "evasao"]].corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
        fig.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

        st.markdown("---")
        st.write("Gere o gráfico de dispersão abaixo para visualizar nota x presença colorido por evasão.")

        b_left, b_center, b_right = st.columns([0.3, 0.4, 0.3])
        with b_center:
            gerar = st.button("🔍 Gerar Gráfico de Dispersão")

        if gerar:
            st.markdown("#### 🔎 Dispersão: Nota vs Presença (%)")
            fig, ax = plt.subplots(figsize=(8, 4.5))
            sns.scatterplot(
                data=df,
                x="nota",
                y="percentual_presenca",
                hue="evasao",
                palette="coolwarm",
                s=50,
                ax=ax
            )
            fig.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)

        # 🔥 Árvore de decisão adicionada abaixo
        st.markdown("---")
        st.markdown("### 🌳 Árvore de Decisão Utilizada no Modelo")

        fig_arvore = gerar_figura_arvore(modelo)
        st.pyplot(fig_arvore, use_container_width=True)
