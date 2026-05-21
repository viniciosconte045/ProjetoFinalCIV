import mysql.connector

def login():
    conexao = conectar()
    cursor = conexao.cursor()

    usuario = input("digite seu nome de usuário:").strip()

    senha = input("digite sua senha:").strip()

    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario = %s AND senha = %s", 
        (usuario, senha)
    )

    resultado = cursor.fetchone()

    if resultado:
        print("Login realizado com sucesso!")
    else:
        print("Usuário ou senha incorretos.")

    if resultado:
        tipo = resultado[0]



