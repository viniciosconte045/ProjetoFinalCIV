import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Senac2026",
        database="escola_db"
    )

def cadastrar_aluno():
    conexao = conectar()
    cursor = conexao.cursor()

    nome = input("Digite seu nome  ").strip()
    idade = input("Digite sua idade em números  ").strip()
    print("Opções de turma: \n 1: 1° EM DS \n 2: 1° EM multimídia \n 3: 1° EM Jogos Digitais \n 4: 2° EM Multimídia \n 5: 2° EM Jogos digitais \n 6: 3° EM Jogos Digitais")
    turma = {
        "1": "1° EM DS",
        "2": "1° EM Multimídia",
        "3": "1° EM Jogos Digitais",
        "4": "2° EM Multimídia",
        "5": "2° EM Jogos Digitais",
        "6": "3° EM Jogos Digitais"
    }
    opcao_turma = input("Digite o numero da sua turma:").strip()
    if opcao_turma not in turma:
        print("Turma inválida")
        return
    elif nome == "" or idade == "":
        print("preencha todos os campos")
        return
    elif not idade.isdigit() or int(idade) <= 0:
        print("idade deve ser um número valido")

    else:
        cursor.execute(
            "INSERT INTO alunos (nome, idade, turma) VALUES (%s, %s, %s)",
            (nome, int(idade), turma[opcao_turma])
        )
        conexao.commit()
        print("Aluno cadastrado")
    cursor.close()
    conexao.close()

def listar_alunos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    for aluno in alunos:
        print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Idade: {aluno[2]}, Turma: {aluno[3]}")
    cursor.close()
    conexao.close()

#def editar_aluno():
    # n sei pq mas deu erro então vou averiguar e arrumar dps conexao = conectar()
    # cursor = conexao.cursor()
    # id_aluno = input("digite o ID do aluno que você quer editar:").strip()
    # if not id_aluno.isdigit():
    #     print("ID deve ser um número válido")
    # else: 
    #     cursor.execute("SELECT * FROM alunos WHERE id_aluno = %s", (id_aluno,))
    #     aluno = cursor.fetchone()
    #     if aluno:
    #         print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Idade: {aluno[2]}, Turma: {aluno[3]}")
    #     else:
    #         print("Aluno não encontrado")
    # cursor.close()
    # conexao.close()
