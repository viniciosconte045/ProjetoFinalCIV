import mysql.connector


def criar_banco():

    conexao = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Senac2026"
    )
    cursor = conexao.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS escola_db")
    cursor.execute("USE escola_db")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INT AUTO_INCREMENT PRIMARY KEY,
        usuario VARCHAR(50) UNIQUE NOT NULL,
        senha VARCHAR(100) NOT NULL,
        tipo ENUM('admin','professor','aluno') NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id_aluno INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        idade INT NOT NULL,
        turma VARCHAR(50) NOT NULL,
        id_usuario INT,
        FOREIGN KEY (id_usuario)
        REFERENCES usuarios(id_usuario)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS professores (
        id_professor INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        disciplina VARCHAR(100),
        id_usuario INT,
        FOREIGN KEY (id_usuario)
        REFERENCES usuarios(id_usuario)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notas (
        id_nota INT AUTO_INCREMENT PRIMARY KEY,
        id_aluno INT NOT NULL,
        nota FLOAT NOT NULL,
        FOREIGN KEY (id_aluno)
        REFERENCES alunos(id_aluno)
        ON DELETE CASCADE
    )
    """)

    cursor.execute("""
    INSERT IGNORE INTO usuarios (usuario, senha, tipo)
    VALUES ('adm', 'josefa', 'admin')
    """)

    cursor.execute("""
    INSERT IGNORE INTO usuarios (usuario, senha, tipo)
    VALUES ('prof', 'josealdo', 'professor')
    """)

    conexao.commit()

    cursor.close()
    conexao.close()

def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Senac2026",
        database="escola_db"
    ) 
    
  