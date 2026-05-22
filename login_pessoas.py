import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Senac2026",
        database="escola_db"
    )

adm_credenciais = {
    "bruno": "Josefa123"
}

def login_adm():
    
    conexao = conectar()

    cursor = conexao.cursor()

    



