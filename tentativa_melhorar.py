import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Senac2026",
        database="escola_db"
    )

def cadastrar_aluno(turma_atual):
    conexao = conectar()
    cursor = conexao.cursor()

    nome = input("Digite nome do aluno:  ").strip()

    idade = input("Digite idade do aluno:  ").strip()

    if not nome.replace(" ", "").isalpha(): 
        print("Nome invalido\n")

    elif not idade.isdigit() or int(idade) <= 0:
        print("idade deve ser um número valido\n")

    else:
        cursor.execute(
            "INSERT INTO alunos (nome, idade, turma) VALUES (%s, %s, %s)",
            (nome, int(idade), turma_atual)
        )

        conexao.commit()

        print("Aluno cadastrado\n")

    cursor.close()

    conexao.close()

def listar_alunos(turma):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
    "SELECT * FROM alunos WHERE turma = %s ORDER BY nome",
    (turma,)
    )
    
    alunos = cursor.fetchall()

    if len(alunos) == 0:
        print("\nNenhum aluno cadastrado\n")
    
    for aluno in alunos:
        print(f"\nID: {aluno[0]},    Nome: {aluno[1]},    Idade: {aluno[2]},   Turma: {aluno[3]}\n")

    cursor.close()

    conexao.close()

def editar_aluno(turma_atual):

    conexao = conectar()

    cursor = conexao.cursor()


    listar_alunos(turma_atual)

    id_aluno = input("digite o ID do aluno que você quer editar: ").strip()

    if not id_aluno.isdigit():
        print("ID deve ser um número válido \n")

    else: 
        cursor.execute("SELECT * FROM alunos WHERE id_aluno = %s AND turma = %s", (id_aluno, turma_atual))
        aluno = cursor.fetchone()

        if aluno:
            print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Idade: {aluno[2]}, Turma: {aluno[3]}")

            novo_nome = input("Digite o novo nome do aluno (reescreva o nome caso queira mante-lo)\n:").strip()

            nova_idade = input("digite a nova idade do aluno (redigite a idade caso queira mante-la)\n:").strip()
            
            if novo_nome == "":
                novo_nome = aluno[1]

            if nova_idade == "":
                nova_idade = aluno[2]

            
            if not str(novo_nome).replace(" ", "").isalpha():
                print("Nome inválido\n")

            
            elif not str(nova_idade).isdigit() or int(nova_idade) <= 0:
                print("Idade deve ser um número válido\n")

            else:

                cursor.execute(
                "UPDATE alunos SET nome = %s, idade = %s WHERE id_aluno = %s",
                (novo_nome, int(nova_idade), id_aluno))

                conexao.commit()

                print("Aluno atualizado\n")


        else:
            print("Aluno não encontrado\n")

    cursor.close()

    conexao.close()

def excluir_aluno(turma_atual): #ultima parte que eu venécios terei que fazer
    conexao = conectar()

    cursor = conexao.cursor()

    listar_alunos(turma_atual)

    id_aluno = input("digite o ID do aluno que você quer excluir: \n").strip()

    if not id_aluno.isdigit():
        print("ID deve ser um número válido\n")

    else:
        cursor.execute("SELECT * FROM alunos WHERE id_aluno = %s AND turma = %s", (id_aluno, turma_atual))

        aluno = cursor.fetchone()

        if aluno:

            cursor.execute("DELETE FROM alunos WHERE id_aluno = %s AND turma = %s", (id_aluno, turma_atual))

            conexao.commit()

            print("Aluno excluído\n")

        else:
            print("Aluno não encontrado\n")

    cursor.close()

    conexao.close()

notas_aluno = []

def adicionar_nota(turma_atual):

    conexao = conectar()
    cursor = conexao.cursor()

    listar_alunos(turma_atual)

    id_aluno = input("Digite o ID do aluno: ").strip()
    
    if not id_aluno.isdigit():
        print("ID inválido\n")
        cursor.close()
        conexao.close()
        return
        
    else: 
    
        cursor.execute(
            "SELECT * FROM alunos WHERE id_aluno = %s AND turma = %s",
            (id_aluno, turma_atual)
        )

    aluno = cursor.fetchone()

    nota = input("Digite a nota: ").strip().replace(",", ".")

    if not aluno:
        print("Aluno não encontrado\n")

    elif not nota.replace(".", "", 1).isdigit():
        print("Nota inválida\n")

    elif float(nota) < 0 or float(nota) > 10:
        print("A nota precisa ser entre 0 e 10\n")

    else:

        cursor.execute(
            "INSERT INTO notas (id_aluno, nota) VALUES (%s, %s)",
            (int(id_aluno), float(nota))
        )

        conexao.commit()

        print("Nota adicionada!\n")

    cursor.close()
    conexao.close()

# remover nota

def remover_nota(turma_atual):

    conexao = conectar()
    cursor = conexao.cursor()

    listar_alunos(turma_atual)

    id_aluno = input("Digite o ID do aluno: ").strip()

    if not id_aluno.isdigit():
        print("ID inválido\n")
        cursor.close()
        conexao.close()
        return

    cursor.execute(
    "SELECT id_nota, nota FROM notas WHERE id_aluno = %s",
    (id_aluno,)
    )

    notas = cursor.fetchall()

    if len(notas) == 0:
        print("Esse aluno não possui notas cadastradas\n")
        cursor.close()
        conexao.close()
        return

    for nota in notas:
        print(f"ID da Nota: {nota[0]} - Nota: {nota[1]}")

    id_nota = input("Digite o ID da nota que deseja remover: ").strip()

    if not id_nota.isdigit():
        print("ID inválido\n")
        cursor.close()
        conexao.close()
        return

    cursor.execute(
        "SELECT * FROM notas WHERE id_nota = %s AND id_aluno = %s",
        (id_nota, id_aluno)
    )

    nota = cursor.fetchone()


    if not nota:
        print("Nota não encontrada\n")

    else:

        cursor.execute(
            "DELETE FROM notas WHERE id_nota = %s",
        (id_nota,)
    )

        conexao.commit()
        print("Nota removida com sucesso\n")

    
    cursor.close()
    conexao.close()

# calcular média
def calcular_media(turma_atual):

    conexao = conectar()
    cursor = conexao.cursor()

    listar_alunos(turma_atual)

    id_aluno = input("Digite o ID do aluno: ").strip()

    if not id_aluno.isdigit():
        print("ID inválido")
        cursor.close()
        conexao.close()
        return 0


    cursor.execute(
        "SELECT AVG(nota) FROM notas WHERE id_aluno = %s ",
        (id_aluno,)
    )


    resultado = cursor.fetchone()

    if resultado is None or resultado[0] is None:
        cursor.close()
        conexao.close()
        return 0

    media = resultado[0]

    cursor.close()
    
    conexao.close()

    if media is None:
        return 0

    return round(media, 2)

# verificar situação do aluno
def verificar_status(turma_atual):

    media = calcular_media(turma_atual)

    if media >= 7:
        return "Aprovado"

    elif media >= 5:
        return "Recuperacao"

    else:
        return "Reprovado"


# mostrar boletim completo
def mostrar_boletim(turma_atual):

    conexao = conectar()
    cursor = conexao.cursor()

    listar_alunos(turma_atual)

    id_aluno = input("Digite o ID do aluno: ").strip()

    if not id_aluno.isdigit():
        print("ID inválido\n")
        cursor.close()
        conexao.close()
        return

    cursor.execute(
        "SELECT * FROM alunos WHERE id_aluno = %s AND turma = %s",
        (id_aluno, turma_atual)
    )

    aluno = cursor.fetchone()
    

    if not aluno:
        print("Aluno não encontrado")
        cursor.close()
        conexao.close()
        return


    cursor.execute(
        "SELECT nota FROM notas WHERE id_aluno = %s",
        (id_aluno,)
    )

    notas = cursor.fetchall()

    print("\n======== BOLETIM ========")

    if len(notas) == 0:

        print("Nenhuma nota cadastrada")

    else:

        lista_notas = [nota[0] for nota in notas]

        print("Notas do aluno:", lista_notas)

        cursor.execute(
            "SELECT AVG(nota) FROM notas WHERE id_aluno = %s",
            (id_aluno,)
        )

        media = cursor.fetchone()[0]

        print("Media final:", round(media, 2))

        if media >= 7:
            print("Situacao: Aprovado")

        elif media >= 5:
            print("Situacao: Recuperacao")

        else:
            print("Situacao: Reprovado")

    print("=========================\n")

    cursor.close()
    conexao.close()


def login():

    professor = {
        "prof": "zion",
    }

    admin = {
        "admin": "josefa",
    }

    nome_usua = input("\nDigite o nome do usuario: ").strip()
    senha_usua = input("\nDigite a senha do usuario: ").strip()

    if nome_usua == "":
        print("Nome de usuario não pode ser vazio\n")
        return None

    if senha_usua == "":
        print("Senha não pode ser vazia\n")
        return None

    if nome_usua in professor and senha_usua == professor[nome_usua]:
        print("Login de professor bem-sucedido\n")
        return "professor"

    elif nome_usua in admin and senha_usua == admin[nome_usua]:
        print("Login de admin bem-sucedido\n")
        return "admin"

    else:
        print("Login falhou, tente novamente\n")
        return None
    
 


    
def menu_adm(turma_atual):

    while True:

        print("\n===== MENU =====")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Editar aluno")
        print("4 - Excluir aluno")
        print("5 - Voltar à seleção de turmas")
        print("6 - Voltar ao login\n")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno(turma_atual)

        elif opcao == "2":
            listar_alunos(turma_atual   )

        elif opcao == "3":
            editar_aluno(turma_atual)

        elif opcao == "4":
            excluir_aluno(turma_atual)

        elif opcao == "5":
            print("Voltando a seleção de turmas")
            return

        elif opcao == "6":
            print("voltando ao login")
            break

        else:
            print("Opção inválida")

def menu_professor(turma_atual):

    while True:

        print("\n===== MENU =====")
        print("1 - Listar alunos")
        print("2 - Adicionar nota")
        print("3 - Remover nota")
        print("4 - Calcular média")
        print("5 - Verificar status")
        print("6 - Mostrar boletim")
        print("7 - Trocar de turma")
        print("8 - Voltar ao login\n")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_alunos(turma_atual)

        elif opcao == "2":
            adicionar_nota(turma_atual)

        elif opcao == "3":
            remover_nota(turma_atual)

        elif opcao == "4":
            print("Media:", calcular_media(turma_atual))

        elif opcao == "5":
            print("Status:", verificar_status(turma_atual))

        elif opcao == "6":
            mostrar_boletim(turma_atual)

        elif opcao == "7":
            print("Voltando à seleção de turmas")
            return


        elif opcao == "8":
            print("Voltando ao login")
            return "login"

        else:
            print("Opção inválida")
        
def selecionar_turma():

    print("\nOpções de turma:")
    print("1 - 1° EM DS")
    print("2 - 1° EM Multimídia")
    print("3 - 1° EM Jogos Digitais")
    print("4 - 2° EM Multimídia")
    print("5 - 2° EM Jogos Digitais")
    print("6 - 3° EM Jogos Digitais")
    turmas = {
    "1": "1° EM DS",
    "2": "1° EM Multimídia",
    "3": "1° EM Jogos Digitais",
    "4": "2° EM Multimídia",
    "5": "2° EM Jogos Digitais",
    "6": "3° EM Jogos Digitais"
    }

    opcao = input("Escolha a turma: ").strip()
    if opcao in turmas:
        return turmas[opcao]

    print("Turma inválida")
    return None

def menus():

    while True:

        print("\n===== SISTEMA ESCOLAR =====")
        print("1 - Fazer login")
        print("2 - Sair\n")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":


            tipo = login()

            if tipo == "admin":
                turma_atual = selecionar_turma()

                if turma_atual:
                    menu_adm(turma_atual)
                else:
                    continue

            elif tipo == "professor":


                while True:
                    turma_atual = selecionar_turma()

                    if not turma_atual:
                        break

                    resultado = menu_professor(turma_atual)

                    if resultado == "login":
                        break
                    
                
            
            
        elif escolha == "2":
            print("Programa encerrado")
            break

        else:
            print("Opção inválida")
menus()
