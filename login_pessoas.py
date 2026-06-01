import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Senac2026",
        database="escola_db"
    )


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

    nome = input("Digite seu nome  ").strip()

    idade = input("Digite sua idade em números  ").strip()

    print("Opções de turma: \n 1: 1° EM DS \n 2: 1° EM multimídia \n 3: 1° EM Jogos Digitais \n 4: 2° EM Multimídia \n 5: 2° EM Jogos digitais \n 6: 3° EM Jogos Digitais")
    turmas = {

        "1": "1° EM DS",
        "2": "1° EM Multimídia",
        "3": "1° EM Jogos Digitais",
        "4": "2° EM Multimídia",
        "5": "2° EM Jogos Digitais",
        "6": "3° EM Jogos Digitais"
    }
    opcao_turma = input("Digite o numero da sua turma:").strip()

    if opcao_turma not in turmas:
        print("Turma inválida")

    elif not nome.replace(" ", "").isalpha(): 
        print("Nome invalido")

    elif not idade.isdigit() or int(idade) <= 0:
        print("idade deve ser um número valido")

    else:
        cursor.execute(
            "INSERT INTO alunos (nome, idade, turma) VALUES (%s, %s, %s)",
            (nome, int(idade), turmas[opcao_turma])
        )

        conexao.commit()

        print("Aluno cadastrado")

    cursor.close()

    conexao.close()

def listar_alunos():
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    alunos = cursor.fetchall()

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado")
    
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

    id_aluno = input("digite o ID do aluno que você quer editar:").strip()

    if not id_aluno.isdigit():
        print("ID deve ser um número válido")

    else: 
        cursor.execute("SELECT * FROM alunos WHERE id_aluno = %s", (id_aluno,))
        aluno = cursor.fetchone()

        if aluno:
            print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Idade: {aluno[2]}, Turma: {aluno[3]}")

            novo_nome = input("Digite o novo nome do aluno (reescreva o nome caso queira mante-lo):").strip()

            nova_idade = input("digite a nova idade do aluno (redigite a idade caso queira mante-la):").strip()

            print("Opções de turma: \n 1: 1° EM DS \n 2: 1° EM multimídia \n 3: 1° EM Jogos Digitais \n 4: 2° EM Multimídia \n 5: 2° EM Jogos digitais \n 6: 3° EM Jogos Digitais")
            
            nova_turma = input("digite o numero da nova turma (redigite o número caso queira mante-lo):").strip()

            if novo_nome == "" or nova_idade == "" or nova_turma == "":
                print("Preencha todos os campos")

            
            elif not novo_nome.replace(" ", "").isalpha():
                print("Nome inválido")

            elif nova_turma not in ["1", "2", "3", "4", "5", "6"]:
                print("Turma inválida")
            
            elif not nova_idade.isdigit() or int(nova_idade) <= 0:
                print("Idade deve ser um número válido")

            else:

                cursor.execute(
                "UPDATE alunos SET nome = %s, idade = %s, turma = %s WHERE id_aluno = %s",
                (novo_nome, int(nova_idade), turmas[nova_turma], id_aluno))

                conexao.commit()

                print("Aluno atualizado")


        else:
            print("Aluno não encontrado")

    cursor.close()

    conexao.close()

def excluir_aluno(): #ultima parte que eu venécios terei que fazer
    conexao = conectar()

    cursor = conexao.cursor()

    id_aluno = input("digite o ID do aluno que você quer excluir:").strip()

    if not id_aluno.isdigit():
        print("ID deve ser um número válido")

    else:
        cursor.execute("SELECT * FROM alunos WHERE id_aluno = %s", (id_aluno,))

        aluno = cursor.fetchone()

        if aluno:

            cursor.execute("DELETE FROM alunos WHERE id_aluno = %s", (id_aluno,))

            conexao.commit()

            print("Aluno excluído")

        else:
            print("Aluno não encontrado")

    cursor.close()

    conexao.close()

# é para começar a programar o sistema de notas apartir desse comentario, o código n vai dar o resultado no terminar pq n tem 
# o menu ainda só no final do cod a gente vai poder corrigir de uma forma "melhor" recomendo testar o codigo em outro arquivo no vscode
#para ir vendo o progresso e depois de terminar por favor  cole o codigo no cod_alunos_adc para o igor poder fazer o menu

# sistema de boletim escolar

notas_aluno = []

# adicionar nota
def adicionar_nota():

    nota = float(input("Digite a nota: "))

    if nota >= 0 and nota <= 10:
        notas_aluno.append(nota)
        print("Nota adicionada!\n")

    else:
        print("A nota precisa ser entre 0 e 10\n")


# remover nota
def remover_nota():

    if len(notas_aluno) == 0:
        print("Nao existem notas cadastradas\n")

    else:
        print("Notas:", notas_aluno)

        nota_remover = float(input("Digite a nota que deseja remover: "))

        if nota_remover in notas_aluno:
            notas_aluno.remove(nota_remover)
            print("Nota removida com sucesso\n")

        else:
            print("Nota nao encontrada\n")


# calcular média
def calcular_media():

    if len(notas_aluno) == 0:
        return 0

    soma_notas = 0

    for nota in notas_aluno:
        soma_notas = soma_notas + nota

    media = soma_notas / len(notas_aluno)

    return media


# verificar situação do aluno
def verificar_status():

    media = calcular_media()

    if media >= 7:
        return "Aprovado"

    elif media >= 5:
        return "Recuperacao"

    else:
        return "Reprovado"


# mostrar boletim completo
def mostrar_boletim():

    print("\n======== BOLETIM ========")

    if len(notas_aluno) == 0:
        print("Nenhuma nota cadastrada")

    else:
        print("Notas do aluno:", notas_aluno)

        media_final = calcular_media()

        print("Media final:", round(media_final, 2))

        status = verificar_status()

        print("Situacao:", status)

    print("=========================\n")



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
        return "professor" and menu_professor()

    if nome_usua in admin and senha_usua == admin[nome_usua]:
        print("Login de admin bem-sucedido\n")
        return "admin" and menu_admin()
    cursor.execute("SELECT nome, senha FROM alunos")

    def menu_professor():
        print("Bem-vindo, professor! Aqui estão as opções do menu:\n")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Adicionar nota")
        print("4. Remover nota")
        print("5. Mostrar boletim")
        print("6. sair")
        if input("Digite o número da opção desejada: ") == "1":
            cadastrar_aluno()
        elif input("Digite o número da opção desejada: ") == "2":
            listar_alunos()
        elif input("Digite o número da opção desejada: ") == "3":
            adicionar_nota()
        elif input("Digite o número da opção desejada: ") == "4":
            remover_nota()
        elif input("Digite o número da opção desejada: ") == "5":
            mostrar_boletim()
        elif input("Digite o número da opção desejada: ") == "6":
            print("Saindo do sistema...\n")
        else:
            print("Opção inválida\n")





    def menu_admin():
        print("Bem-vindo, admin! Aqui estão as opções do menu:\n")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Editar aluno")
        print("4. Excluir aluno")
        print("5. sair")
        if input("Digite o número da opção desejada: ") == "1":
            cadastrar_aluno()
        elif input("Digite o número da opção desejada: ") == "2":
            listar_alunos()
        elif input("Digite o número da opção desejada: ") == "3":
            editar_aluno()
        elif input("Digite o número da opção desejada: ") == "4":
            excluir_aluno()
        elif input("Digite o número da opção desejada: ") == "5":
            print("Saindo do sistema...\n")
        else:
            print("Opção inválida\n")
        
