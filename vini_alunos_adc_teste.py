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

    nome = input("Digite o nome do aluno:  ").strip()

    idade = input("Digite a idade do aluno em números:  ").strip()

    senha = input("Dgite a senha do aluno:  ").strip()

    print("Opções de turma: \n 1: 1° EM DS \n 2: 1° EM multimídia \n 3: 1° EM Jogos Digitais \n 4: 2° EM Multimídia \n 5: 2° EM Jogos digitais \n 6: 3° EM Jogos Digitais \n")
    turmas = {

        "1": "1° EM DS",
        "2": "1° EM Multimídia",
        "3": "1° EM Jogos Digitais",
        "4": "2° EM Multimídia",
        "5": "2° EM Jogos Digitais",
        "6": "3° EM Jogos Digitais"
    }
    opcao_turma = input("Digite o numero da turma:  ").strip()

    if opcao_turma not in turmas:
        print("Turma inválida\n")

    elif not nome.replace(" ", "").isalpha(): 
        print("Nome invalido\n")

    elif not idade.isdigit() or int(idade) <= 0:
        print("idade deve ser um número valido\n")

    elif senha == "":
        print("Senha não pode ser vazia\n")

    elif len (senha) < 3:
        print("Senha deve ter pelo menos 3 caracteres")

    elif senha.isspaace():
        print("Senha não pode ser apenas espaços\n") # se pá é desnecessário, mas é melhor ter

    elif ( " " in senha):
        print("Senha não pode conter espaços\n")

    else:
        cursor.execute(
            "INSERT INTO alunos (nome, idade, turma) VALUES (%s, %s, %s)",
            (nome, int(idade), turmas[opcao_turma])
        )

        conexao.commit()

        print("Aluno cadastrado\n")

    cursor.close()

    conexao.close()

def listar_alunos():
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    alunos = cursor.fetchall()

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado\n")
    
    for aluno in alunos:
        print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Idade: {aluno[2]}, Turma: {aluno[3]}")

    cursor.close()

    conexao.close()

def editar_aluno():

    conexao = conectar()

    cursor = conexao.cursor()

    turmas = {

    "1": "1° EM DS",
    "2": "1° EM Multimídia",
    "3": "1° EM Jogos Digitais",
    "4": "2° EM Multimídia",
    "5": "2° EM Jogos Digitais",
    "6": "3° EM Jogos Digitais"
}

    id_aluno = input("digite o ID do aluno que você quer editar: \n").strip()

    if not id_aluno.isdigit():
        print("ID deve ser um número válido \n")

    else: 
        cursor.execute("SELECT * FROM alunos WHERE id_aluno = %s", (id_aluno,))
        aluno = cursor.fetchone()

        if aluno:
            print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Idade: {aluno[2]}, Turma: {aluno[3]}")

            novo_nome = input("Digite o novo nome do aluno (reescreva o nome caso queira mante-lo)\n:").strip()

            nova_idade = input("digite a nova idade do aluno (redigite a idade caso queira mante-la)\n:").strip()

            print("Opções de turma: \n 1: 1° EM DS \n 2: 1° EM multimídia \n 3: 1° EM Jogos Digitais \n 4: 2° EM Multimídia \n 5: 2° EM Jogos digitais \n 6: 3° EM Jogos Digitais\n")
            
            nova_turma = input("digite o numero da nova turma (redigite o número caso queira mante-lo): \n").strip()

            if novo_nome == "" or nova_idade == "" or nova_turma == "":
                print("Preencha todos os campos\n")

            
            elif not novo_nome.replace(" ", "").isalpha():
                print("Nome inválido\n")

            elif nova_turma not in ["1", "2", "3", "4", "5", "6"]:
                print("Turma inválida")
            
            elif not nova_idade.isdigit() or int(nova_idade) <= 0:
                print("Idade deve ser um número válido\n")

            else:

                cursor.execute(
                "UPDATE alunos SET nome = %s, idade = %s, turma = %s WHERE id_aluno = %s",
                (novo_nome, int(nova_idade), turmas[nova_turma], id_aluno))

                conexao.commit()

                print("Aluno atualizado\n")


        else:
            print("Aluno não encontrado\n")

    cursor.close()

    conexao.close()

def excluir_aluno(): #ultima parte que eu venécios terei que fazer, erá mentira, eu fui enganado por meus conecimentos, maldito homem que acredita em mim si proprio
    conexao = conectar()

    cursor = conexao.cursor()

    id_aluno = input("digite o ID do aluno que você quer excluir: \n").strip()

    if not id_aluno.isdigit():
        print("ID deve ser um número válido\n")

    else:
        cursor.execute("SELECT * FROM alunos WHERE id_aluno = %s", (id_aluno,))

        aluno = cursor.fetchone()

        if aluno:

            cursor.execute("DELETE FROM alunos WHERE id_aluno = %s", (id_aluno,))

            conexao.commit()

            print("Aluno excluído\n")

        else:
            print("Aluno não encontrado\n")

    cursor.close()

    conexao.close()


