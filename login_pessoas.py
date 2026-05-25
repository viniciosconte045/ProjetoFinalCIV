import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Senac2026",
        database="escola_db"
    )

def login():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        # Solicita ID do usuário
        try:
            id_usuario = int(input("ID do Usuário: ").strip())
        except ValueError:
            print("ID inválido! Deve ser um número.")
            return

        senha = input("Senha: ").strip()

        # Busca usuário pelo ID e valida senha
        cursor.execute(
            "SELECT id, tipo_usuario FROM usuarios WHERE id = %s AND senha = %s",
            (id_usuario, senha)
        )

        resultado = cursor.fetchone()

        if resultado:
            id_resultado, tipo_usuario = resultado
            print("Login realizado com sucesso!")

            # Direciona para menu conforme tipo de usuário
            if tipo_usuario == "aluno":
                menu_aluno()
            elif tipo_usuario == "professor":
                menu_professor()
            elif tipo_usuario == "admin":
                menu_admin()
            else:
                print(f"Tipo de usuário desconhecido: {tipo_usuario}")

        else:
            print("ID ou senha inválidos")

        cursor.close()
        conexao.close()

    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
    except Exception as erro:
        print(f"Erro inesperado: {erro}")
    



