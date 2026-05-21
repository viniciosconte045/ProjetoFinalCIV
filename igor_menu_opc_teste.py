import mysql.connector



def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Senac2026",
        database="escola_db"
    )

def cadastrar_aluno(): #função do administrador
    conexao = conectar()

    cursor = conexao.cursor()

    nome = input("Digite seu nome:  ").strip()

    idade = input("Digite sua idade em números:  ").strip()

    print("Opções de turma: \n 1: 1° EM DS \n 2: 1° EM multimídia \n 3: 1° EM Jogos Digitais \n 4: 2° EM Multimídia \n 5: 2° EM Jogos digitais \n 6: 3° EM Jogos Digitais \n")
    turmas = {

        "1": "1° EM DS",
        "2": "1° EM Multimídia",
        "3": "1° EM Jogos Digitais",
        "4": "2° EM Multimídia",
        "5": "2° EM Jogos Digitais",
        "6": "3° EM Jogos Digitais"
    }
    opcao_turma = input("Digite o numero da sua turma:  ").strip()

    if opcao_turma not in turmas:
        print("Turma inválida\n")

    elif not nome.replace(" ", "").isalpha(): 
        print("Nome invalido\n")

    elif not idade.isdigit() or int(idade) <= 0:
        print("idade deve ser um número valido\n")

    else:
        cursor.execute(
            "INSERT INTO alunos (nome, idade, turma) VALUES (%s, %s, %s)",
            (nome, int(idade), turmas[opcao_turma])
        )

        conexao.commit()

        print("Aluno cadastrado\n")

    cursor.close()

    conexao.close()

def listar_alunos(): #função do administrador e do professor
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

def editar_aluno(): #função do administrador

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

def excluir_aluno(): #função do administrador
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

notas_aluno = []

# adicionar nota
def adicionar_nota(): #função do professor

    nota = float(input("Digite a nota: "))

    if nota >= 0 and nota <= 10:
        notas_aluno.append(nota)
        print("Nota adicionada!\n")

    else:
        print("A nota precisa ser entre 0 e 10\n")


# remover nota
def remover_nota(): #função do professor

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
def calcular_media(): #função do aluno

    if len(notas_aluno) == 0:
        return 0

    soma_notas = 0

    for nota in notas_aluno:
        soma_notas = soma_notas + nota

    media = soma_notas / len(notas_aluno)

    return media


# verificar situação do aluno
def verificar_status(): #função do professor e do aluno

    media = calcular_media()

    if media >= 7:
        return "Aprovado"

    elif media >= 5:
        return "Recuperacao"

    else:
        return "Reprovado"


# mostrar boletim completo
def mostrar_boletim(): #função do professor e do aluno

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




# fim do codigo
# acho q ficou bom 👍
 