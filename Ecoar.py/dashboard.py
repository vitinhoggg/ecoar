import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from modelo import carregar_modelo_e_dados

# Definindo tema para consistência
sns.set_theme(style="whitegrid", rc={"figure.dpi": 100})

def mostrar_dashboard():
    # Cabeçalho local (abaixo do título principal do app)
    st.markdown("### 📈 Visão Geral dos Dados Acadêmicos")
    st.write(
        "Explore abaixo as distribuições e correlações entre as variáveis que influenciam o risco de evasão estudantil."
    )

    # Carrega modelo e dados
    modelo, df = carregar_modelo_e_dados()

    # Pequeno espaço superior
    st.markdown("<br>", unsafe_allow_html=True)

    # Container centralizado: cria 3 colunas e usa a do meio como área principal
    left, center, right = st.columns([0.08, 0.84, 0.08])

    with center:
        # Linha com dois gráficos lado a lado (notas e presença)
        st.markdown("#### 📊 Distribuições")
        gcol1, gcol2 = st.columns(2, gap="large")

        # Gráfico 1 - Distribuição das Notas
        with gcol1:
            st.markdown("**📘 Distribuição das Notas**")
            fig, ax = plt.subplots(figsize=(6, 3.5))
            sns.histplot(df["nota"], kde=True, ax=ax, color="#1f77b4")
            ax.set_xlabel("Nota")
            ax.set_ylabel("Frequência")
            ax.grid(alpha=0.25)
            fig.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)

        # Gráfico 2 - Distribuição da Presença
        with gcol2:
            st.markdown("**🟠 Distribuição da Presença (%)**")
            fig, ax = plt.subplots(figsize=(6, 3.5))
            sns.histplot(df["percentual_presenca"], kde=True, ax=ax, color="#ff7f0e")
            ax.set_xlabel("Presença (%)")
            ax.set_ylabel("Frequência")
            ax.grid(alpha=0.25)
            fig.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)

        # Separador
        st.markdown("---")

        # Heatmap centralizado
        st.markdown("#### 🔗 Correlação entre Variáveis")
        fig, ax = plt.subplots(figsize=(8, 4))
        corr = df[["idade", "nota", "percentual_presenca", "evasao"]].corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
        ax.set_title("")  # sem título redundante
        fig.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

        # Separador e instrução
        st.markdown("---")
        st.write("Gere o gráfico de dispersão abaixo para visualizar nota x presença colorido por evasão.")

        # Botão centralizado: colunas com o botão no meio
        b_left, b_center, b_right = st.columns([0.3, 0.4, 0.3])
        with b_center:
            gerar = st.button("🔍 Gerar Gráfico de Dispersão")

        # Ao clicar, exibe o gráfico (centralizado)
        if gerar:
            st.markdown("#### 🔎 Dispersão: Nota vs Presença (%)")
            fig, ax = plt.subplots(figsize=(8, 4.5))
            sns.scatterplot(
                data=df,
                x="nota",
                y="percentual_presenca",
                hue="evasao",
                palette="coolwarm",
                ax=ax,
                s=50,
                edgecolor="w",
                linewidth=0.5
            )
            ax.set_xlabel("Nota")
            ax.set_ylabel("Presença (%)")
            ax.grid(alpha=0.25)
            ax.legend(title="Evasão", loc="best")
            fig.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from modelo import carregar_modelo_e_dados

# Definindo tema para consistência
sns.set_theme(style="whitegrid", rc={"figure.dpi": 100})

def mostrar_dashboard():
    # Cabeçalho local (abaixo do título principal do app)
    st.markdown("### 📈 Visão Geral dos Dados Acadêmicos")
    st.write(
        "Explore abaixo as distribuições e correlações entre as variáveis que influenciam o risco de evasão estudantil."
    )

    # Carrega modelo e dados
    modelo, df = carregar_modelo_e_dados()

    # Pequeno espaço superior
    st.markdown("<br>", unsafe_allow_html=True)

    # Container centralizado: cria 3 colunas e usa a do meio como área principal
    left, center, right = st.columns([0.08, 0.84, 0.08])

    with center:
        # Linha com dois gráficos lado a lado (notas e presença)
        st.markdown("#### 📊 Distribuições")
        gcol1, gcol2 = st.columns(2, gap="large")

        # Gráfico 1 - Distribuição das Notas
        with gcol1:
            st.markdown("**📘 Distribuição das Notas**")
            fig, ax = plt.subplots(figsize=(6, 3.5))
            sns.histplot(df["nota"], kde=True, ax=ax, color="#1f77b4")
            ax.set_xlabel("Nota")
            ax.set_ylabel("Frequência")
            ax.grid(alpha=0.25)
            fig.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)

        # Gráfico 2 - Distribuição da Presença
        with gcol2:
            st.markdown("**🟠 Distribuição da Presença (%)**")
            fig, ax = plt.subplots(figsize=(6, 3.5))
            sns.histplot(df["percentual_presenca"], kde=True, ax=ax, color="#ff7f0e")
            ax.set_xlabel("Presença (%)")
            ax.set_ylabel("Frequência")
            ax.grid(alpha=0.25)
            fig.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)

        # Separador
        st.markdown("---")

        # Heatmap centralizado
        st.markdown("#### 🔗 Correlação entre Variáveis")
        fig, ax = plt.subplots(figsize=(8, 4))
        corr = df[["idade", "nota", "percentual_presenca", "evasao"]].corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
        ax.set_title("")  # sem título redundante
        fig.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

        # Separador e instrução
        st.markdown("---")
        st.write("Gere o gráfico de dispersão abaixo para visualizar nota x presença colorido por evasão.")

        # Botão centralizado: colunas com o botão no meio
        b_left, b_center, b_right = st.columns([0.3, 0.4, 0.3])
        with b_center:
            gerar = st.button("🔍 Gerar Gráfico de Dispersão")

        # Ao clicar, exibe o gráfico (centralizado)
        if gerar:
            st.markdown("#### 🔎 Dispersão: Nota vs Presença (%)")
            fig, ax = plt.subplots(figsize=(8, 4.5))
            sns.scatterplot(
                data=df,
                x="nota",
                y="percentual_presenca",
                hue="evasao",
                palette="coolwarm",
                ax=ax,
                s=50,
                edgecolor="w",
                linewidth=0.5
            )
            ax.set_xlabel("Nota")
            ax.set_ylabel("Presença (%)")
            ax.grid(alpha=0.25)
            ax.legend(title="Evasão", loc="best")
            fig.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)
