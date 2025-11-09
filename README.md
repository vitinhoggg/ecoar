🎓 ECOAR — Sistema de Previsão de Evasão Acadêmica

![WhatsApp Video 2025-11-09 at 00 10 22](https://github.com/user-attachments/assets/05bf8b65-89c4-4955-9839-4e2ddd10f6f8)


📘 Sobre o Projeto

ECOAR é um sistema web interativo desenvolvido em Python com Streamlit, criado para prever o risco de evasão acadêmica de estudantes com base em dados históricos.
O projeto integra visualizações gráficas, análise de dados e um modelo de Machine Learning (Árvore de Decisão) que estima a probabilidade de evasão conforme o desempenho e a presença dos alunos.
ECOAR é um sistema web interativo desenvolvido em Python com Streamlit, criado para prever o risco de evasão acadêmica de estudantes com base em dados históricos.
O projeto integra visualizações gráficas, análise de dados e um modelo de Machine Learning (Árvore de Decisão) que estima a probabilidade de evasão conforme o desempenho e a presença dos alunos.


⚙️ Tecnologias Utilizadas

🐍 Python 3.10+

📊 Streamlit — Interface web interativa

🧠 Scikit-learn — Modelo de Machine Learning

🐬 MySQL — Armazenamento relacional dos dados acadêmicos

🍃 MongoDB — Banco NoSQL para armazenar logs e histórico de previsões

📈 Matplotlib e Seaborn — Visualizações e gráficos

🧾 Pandas — Manipulação e análise de dados


📊 Funcionalidades


🧮 Painel (Dashboard)


Distribuições de notas e presença
Heatmap de correlação entre variáveis
Gráfico de dispersão “Nota x Presença (%)”

🎯 Previsão de Evasão


Entrada de dados: idade, nota e frequência
Retorno imediato:

🔴 Alto risco de evasão

🟢 Baixo risco de evasão

Registro automático da previsão no MongoDB

🧠 Modelo de Machine Learning



O ECOAR utiliza uma Árvore de Decisão (DecisionTreeClassifier) com profundidade limitada (max_depth=3), garantindo explicabilidade e simplicidade.
O modelo é treinado com os dados do banco MySQL, e os resultados são armazenados no MongoDB para consulta posterior.
