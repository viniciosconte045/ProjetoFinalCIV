import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Senac2026",
        database="escola_db"
    )

def login():

    conexao = conectar()

    cursor = conexao.cursor()

    usuario = input("Usuário: ").strip()

    senha = input("Senha: ").strip()

    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario = %s AND senha = %s",
        (usuario, senha)
    )

    resultado = cursor.fetchone()

    if resultado:

        print("Login realizado")

        if usuario == "admin":
            menu_admin()

        elif usuario == "professor":
            menu_professor()

    else:
        print("Usuário ou senha inválidos")

    cursor.close()

    conexao.close()
    



