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
 
        print("\nLista de notas:")
 
        for i in range(len(notas_aluno)):
            print(f"{i} - {notas_aluno[i]}")
 
        indice = int(input("Digite o numero da nota que deseja remover: "))
 
        if indice >= 0 and indice < len(notas_aluno):
 
            notas_aluno.pop(indice)
 
            print("Nota removida com sucesso!\n")
 
        else:
            print("Indice invalido\n")
 
 
# editar nota
def editar_nota():
 
    if len(notas_aluno) == 0:
        print("Nao existem notas cadastradas\n")
 
    else:
 
        print("\nLista de notas:")
 
        for i in range(len(notas_aluno)):
            print(f"{i} - {notas_aluno[i]}")
 
        indice = int(input("Digite o numero da nota que deseja editar: "))
 
        if indice >= 0 and indice < len(notas_aluno):
 
            nova_nota = float(input("Digite a nova nota: "))
 
            if nova_nota >= 0 and nova_nota <= 10:
 
                notas_aluno[indice] = nova_nota
 
                print("Nota atualizada com sucesso!\n")
 
            else:
                print("A nota deve estar entre 0 e 10\n")
 
        else:
            print("Indice invalido\n")
 
 
# calcular média
def calcular_media():
 
    if len(notas_aluno) == 0:
        return 0
 
    soma_notas = 0
 
    for nota in notas_aluno:
        soma_notas = soma_notas + nota
 
    media = soma_notas / len(notas_aluno)
 
    return media
<<<<<<< HEAD
 
 
=======
  

>>>>>>> 380c963f5b91c5e70a94d9363987b7b91ebcc899
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
 
        print("Notas do aluno:")
 
        for nota in notas_aluno:
            print(nota)
 
        media_final = calcular_media()
 
        print("\nMedia final:", round(media_final, 2))
 
        status = verificar_status()
 
        print("Situacao:", status)
 
    print("=========================\n")


<<<<<<< HEAD
# menu principal
while True:
 
    print("\n===== MENU NOTAS =====")
    print("1 - Adicionar nota")
    print("2 - Remover nota")
    print("3 - Editar nota")
    print("4 - Calcular média")
    print("5 - Verificar status")
    print("6 - Mostrar boletim")
    print("7 - Sair")
 
    escolha = input("Escolha uma opção: ")
 
    if escolha == "1":
        adicionar_nota()
 
    elif escolha == "2":
        remover_nota()
 
    elif escolha == "3":
        editar_nota()
 
    elif escolha == "4":
 
        media = calcular_media()
 
        print("Media do aluno:", round(media, 2))
 
    elif escolha == "5":
 
        situacao = verificar_status()
 
        print("Status do aluno:", situacao)
 
    elif escolha == "6":
        mostrar_boletim()
 
    elif escolha == "7":
 
        print("Encerrando sistema...")
        break
 
    else:
        print("Opcao invalida")


# fim do codigo
# acho q ficou bom 👍
=======



# fim do codigo
# acho q ficou bom 👍
 
>>>>>>> 380c963f5b91c5e70a94d9363987b7b91ebcc899
