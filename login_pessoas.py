import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Senac2026",
        database="escola_db"
    )

def login():

    conexao= conectar()
    cursor = conexao.cursor()

    professor = {
        "professor1": "apaga",
    
    }

    admin = {
        "admin1": "josefa",
    }

    nome_usua = input("Digite o nome do usuario: ").strip()
    senha_usua = input ("Digite a senha do usuario: ").strip()

    if senha_usua == "":
        print("Senha não pode ser vazia\n")

    if senha_usua.isspace():
        print("Senha não pode ser apenas espaços\n")

    if nome_usua== "" or nome_usua.isspace():
        print("Nome de usuario não pode ser vazio ou apenas espaços\n")

    if nome_usua == "":
        print("Nome de usuario não pode ser vazio\n")

    if nome_usua.isspace():
        print("Nome de usuario não pode ser apenas espaços\n")

    if nome_usua in professor and senha_usua == professor[nome_usua]:
        print("Login de professor bem-sucedido\n")
        return "professor"

    if nome_usua in admin and senha_usua == admin[nome_usua]:
        print("Login de admin bem-sucedido\n")
        return "admin"
    cursor.execute("SELECT nome, senha FROM alunos")


