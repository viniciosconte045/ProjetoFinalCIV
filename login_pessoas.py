import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Senac2026",
        database="escola_db"
    )

adm_usuario = "Bruno"
adms_senha = "BOA_NOITE_BRUNO"

def login(usuario, senha):
    if usuario == adm_usuario and senha == adms_senha:
        return "Bem vindo, administrador!"
    if usuario == "aluno" and senha == "123456":
        return "Bem vindo, aluno!"
    if usuario == "professor" and senha == "654321":
        return "Bem vindo, professor!"
    else:
        return "Usuário ou senha incorretos"