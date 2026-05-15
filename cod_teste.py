import _mysql_connector 

def conectar():
    return _mysql_connector.connect(
        host= "127.0.0.1",
        user="root",
        password="Senac2026",
        database="escola_db"

    )

def cadatrar_aluno():
    conexão = conectar()
    cursor = conexão.cursor()

    nome = input("Digite seu nome  ").strip()
    idade = input("Digite sua idade em números  ").strip()
    print("Opções de turma: \n 1: 1° EM DS \n 2: 1° EM multimídia \n 3: 1° EM Jogos Digitais \n 4: 2° EM Multimídia \n 5: 2° EM Jogos digitais \n 6: 3° EM Jogos Digitais")
    turma = input("Digite sua turma")
