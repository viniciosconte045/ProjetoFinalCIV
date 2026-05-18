import _mysql_connector 

def conectar():
    return _mysql_connector.connect(
        host= "127.0.0.1",
        user="root",
        password="Senac2026",
        database="escola_db"

    )

def cadastrar_aluno():
    conexão = conectar()
    cursor = conexão.cursor()

    nome = input("Digite seu nome  ").strip()
    idade = input("Digite sua idade em números  ").strip()
    print("Opções de turma: \n 1: 1° EM DS \n 2: 1° EM multimídia \n 3: 1° EM Jogos Digitais \n 4: 2° EM Multimídia \n 5: 2° EM Jogos digitais \n 6: 3° EM Jogos Digitais")
    turma = input("Digite sua turma")
    if turma > 1 or turma < 6 and turma.isdigit():
        print("turma invalida")

    elif nome == "" or idade == "" or turma == "":
        print("preencha todos os campos")
    elif not idade.isdigit() or int(idade) <= 0:
        print("idade deve ser um número valido")
    else:
        cursor.execute("INSERT INTO alunos (nome, idade, turma) VALUES (%s, %s, %s)", (nome, idade, turma))
        conexão.commit()
        print("Aluno cadastrado")
        cursor.close()
        conexão.close()

def listar_alunos():
    conexao = conectar()
    cursor = conexão.cursor()
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    for aluno in alunos:
        print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Idade: {aluno[2]}, Turma: {aluno[3]}")
    cursor.close()
    conexão.close()

def editar_aluno():
    conexão = conectar()


