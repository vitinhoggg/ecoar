import json
import random
from faker import Faker

# 1. Inicializa o Faker
fake = Faker('pt_BR')

# Define algumas constantes
NUM_ALUNOS = 1000000
CARGA_HORARIA_PADRAO = 80 

# LISTA: Nomes dos Cursos/Áreas de Estudo
CURSOS = [
    "Engenharia",
    "ADS",
    "Direito",
    "Administração",
    "Arquitetura",
    "Psicologia",
    "Medicina"
]


def gerar_nota_unica(nome_do_curso):
    """Gera o objeto de nota, usando o nome do curso como a 'disciplina'."""
    
    # Gera uma nota entre 0.0 e 10.0
    nota_final = round(random.uniform(0.0, 10.0), 1) 
    
    # Retorna um ARRAY com apenas UM documento de nota
    # A disciplina é o próprio curso do aluno.
    return [{
        "disciplina": nome_do_curso, 
        "valor": nota_final
    }]

def gerar_frequencia_ficticia(carga_horaria):
    """Gera dados de frequência (faltas e porcentagem)."""
    
    total_faltas = random.randint(0, 20) 
    porcentagem = round((total_faltas / carga_horaria) * 100, 2)
    
    return {
        "total_faltas": total_faltas,
        "carga_horaria_total": carga_horaria,
        "porcentagem_falta": porcentagem
    }

def gerar_documento_aluno(id_aluno):
    """Cria um documento de aluno completo."""
    
    # Gera os dados principais
    nome = fake.name() 
    idade = random.randint(18, 30)
    
    # Escolhe o curso
    curso_aluno = random.choice(CURSOS) 
    semestre = random.randint(1, 8)
    
    # Gera dados aninhados
    # Passa o nome do curso para a função de notas
    notas = gerar_nota_unica(curso_aluno) 
    frequencia = gerar_frequencia_ficticia(CARGA_HORARIA_PADRAO)
    
    # Retorna o documento completo
    return {
        "id_aluno": id_aluno, 
        "nome": nome, 
        "idade": idade,
        "curso": curso_aluno, 
        "semestre": semestre,
        "notas": notas, 
        "frequencia": frequencia
    }

# 3. Geração e Salvamento dos Dados
dados_alunos = []
for i in range(1, NUM_ALUNOS + 1):
    documento = gerar_documento_aluno(i)
    dados_alunos.append(documento)

# 4. Salva o resultado em um arquivo JSON
with open('dados_alunos_ficticios_final.json', 'w', encoding='utf-8') as f:
    json.dump(dados_alunos, f, ensure_ascii=False, indent=2)

print(f"✅ Geração de {NUM_ALUNOS} documentos concluída.")
print("O arquivo 'dados_alunos_ficticios_final.json' foi criado.")
