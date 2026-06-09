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

 #definir_menu() #função do menu, onde todos tem o mesmo menu
def definir_menu():
     
    while True: 
        
     print("\n======== MENU ========")       
      
menu = "menu de administração de alunos e notas"
print(menu)
print("1. Cadastrar aluno (Administrador)")
print("2. Listar alunos (Administrador e Professor)")
print("3. Editar aluno (Administrador)")
print("4. Excluir aluno (Administrador)")
print("5. Adicionar nota (Professor)")
print("6. Remover nota (Professor)")
print("7. Calcular média (Aluno)")
print("8. Verificar situação do aluno (Professor e Aluno)")
print("9. Mostrar boletim completo (Professor e Aluno)")
print("0. Sair")

opcao = input("Digite o número da opção desejada: ").strip()

definir_menu("Digite o número da opção desejada: ")
funçãos = input("Digite o número da opção desejada: ").strip("Digite o número da opção desejada: ")
if funçãos in definir_menu:
 for opcao in definir_menu:
    if funçãos == "1":
            cadastrar_aluno("Digite seu nome:  ", "Digite sua idade em números:  ", "Digite o numero da sua turma:  ")

elif funçãos == "2":
            listar_alunos("Digite o número da opção desejada: ")

elif funçãos == "3":
            editar_aluno("digite o ID do aluno que você quer editar: \n","Digite o novo nome do aluno(reescreva o nome caso queira mante-lo)\n:","digite a nova idade do aluno(redigite a idade caso queira mante-la)\n:","digite o numero da nova turma(redigite o número caso queira mante-lo):\n")    

elif funçãos == "4":
            excluir_aluno("digite o ID do aluno que você quer excluir: \n")

elif funçãos == "5":
            adicionar_nota("Digite a nota: ")

elif funçãos == "6":
            remover_nota("Digite a nota que deseja remover: ")

elif funçãos == "7":
            media = calcular_media("Digite o número da opção desejada: ")
            print(f"A média do aluno é: {media:.2f}\n")

elif funçãos == "8":
            status = verificar_status("Digite o número da opção desejada:")
            print(f"A situação do aluno é: {status}\n")

elif funçãos == "9":
            mostrar_boletim("Digite o número da opção desejada: ")

elif funçãos == "0":
            print("Saindo do programa...") 
else:
            print("Opção inválida, tente novamente.\n")
            definir_menu("Digite o número da opção desejada: ")

            print("Digite o número da opção desejada: ")

            funçãos = input().strip("Digite o número da opção desejada:")

            lupen = "Opção inválida, tente novamente.\n"

            print(lupen)
            calcular_media()
            verificar_status()

            media = calcular_media()

            print(f"A média do aluno é: {media:.2f}\n")
            status = verificar_status()

            print(f"A situação do aluno é: {status}\n")
            media = "calcular média do aluno" \
            "Digite o número da opção desejada: " \
            "Opção inválida, tente novamente.\n" \
            "verificar situação do aluno"

            print(media)
            bolintni = "mostrar boletim completo do aluno" \
            "Digite o número da opção desejada: " \
            "Opção inválida, tente novamente.\n"
            
            print(bolintni)
            menu_do_bolintni = "menu de administração de alunos e notas" \
            "\n1. Cadastrar aluno (Administrador)" \
            "\n2. Listar alunos (Administrador e Professor)"
            "\n3. Editar aluno (Administrador)"
            "\n4. Excluir aluno (Administrador)"
            "\n5. Adicionar nota (Professor)"
            "\n6. Remover nota (Professor)"
            "\n7. Calcular média (Aluno)"
            "\n8. Verificar situação do aluno (Professor e Aluno)"
            "\n9. Mostrar boletim completo (Professor e Aluno)"
            "\n0. Sair"
            print(menu_do_bolintni)
            calcular_media()
            verificar_status()


# siquier mudar vique avontade o codico.
# e so um teste si tiver serto siquiser copie ou si tiver errado mude tudo vique a vontade asinado igor.
# #sitiver no ps5 ou ps4 ou no nitendo o couquer jogo que eu jogo esqueci na steam eu mijamo igor-junio ou igor-junio2010 ou igorjunio e no roblos e igorjunio2010hdhd mais nao jogo tanto 

