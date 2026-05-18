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
    turma = input("Digite sua turma")
    if not turma.isdigit() or int(turma) < 1 or int(turma) > 6:
        print("Turma inválida")

    elif nome == "" or idade == "" or turma == "":
        print("preencha todos os campos")
    elif not idade.isdigit() or int(idade) <= 0:
        print("idade deve ser um número valido")
    else:
        cursor.execute("INSERT INTO alunos (nome, idade, turma) VALUES (%s, %s, %s)", (nome, idade, turma))
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

def editar_aluno():
    conexao = conectar()
    cursor = conexao.cursor()
    id_aluno = input("digite o ID do aluno que você quer editar:").strip()
    if not id_aluno.isdigit():
        print("ID deve ser um número válido")
    else: 
        cursor.execute("SELECT * FROM alunos WHERE id_aluno = %s", (id_aluno,))
        aluno = cursor.fetchone()
        if aluno:
            print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Idade: {aluno[2]}, Turma: {aluno[3]}")
        else:
            print("Aluno não encontrado")
    cursor.close()
    conexao.close()



