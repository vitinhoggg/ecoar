import pandas as pd
import mysql.connector
from sklearn.tree import DecisionTreeClassifier
import streamlit as st

@st.cache_resource
def carregar_modelo_e_dados():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="dados_alunos"
    )

    alunos = pd.read_sql("SELECT * FROM alunos", con)
    notas = pd.read_sql("SELECT * FROM notas", con)
    frequencia = pd.read_sql("SELECT * FROM frequencia", con)
    evasao = pd.read_sql("SELECT * FROM evasao", con)
    disciplinas = pd.read_sql("SELECT * FROM disciplinas", con)

    df = alunos.merge(notas, on='id_aluno') \
               .merge(frequencia, on=['id_aluno', 'id_disciplina']) \
               .merge(evasao, on='id_aluno') \
               .merge(disciplinas, on='id_disciplina')

    df.dropna(inplace=True)

    media_nota = df['nota'].mean()
    media_presenca = df['percentual_presenca'].mean()

    df = df[
        (df['nota'] >= media_nota - 2) & (df['nota'] <= media_nota + 2) &
        (df['percentual_presenca'] >= media_presenca - 20) & (df['percentual_presenca'] <= media_presenca + 20)
    ]

    X = df[['idade', 'nota', 'percentual_presenca']]
    y = df['evasao']

    modelo = DecisionTreeClassifier(max_depth=3)
    modelo.fit(X, y)

    return modelo, df