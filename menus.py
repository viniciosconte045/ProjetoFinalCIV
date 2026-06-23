from alunos import (
    cadastrar_aluno,
    listar_alunos,
    editar_aluno,
    excluir_aluno
)

from notas import (
    adicionar_nota,
    editar_nota,
    remover_nota,
    listar_notas,
    boletim_geral
)

from login import login

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
            return "login"

        else:
            print("Opção inválida")

def menu_professor(turma_atual):

    while True:

        print("\n===== MENU =====")
        print("1 - Listar alunos")
        print("2 - Adicionar nota")
        print("3 - Editar nota")
        print("4 - Remover nota")
        print("5 - Listar notas")
        print("6 - Mostrar boletim Geral")
        print("7 - Trocar de turma")
        print("8 - Voltar ao login\n")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_alunos(turma_atual)

        elif opcao == "2":
            adicionar_nota(turma_atual)

        elif opcao == "3":
            editar_nota(turma_atual)
        elif opcao == "4":
            remover_nota(turma_atual)

        elif opcao == "5":
            listar_notas(turma_atual)

        elif opcao == "6":
            boletim_geral(turma_atual)

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
    "6": "3° EM Jogos Digitais\n"
    }

    opcao = input("\nEscolha a turma: ").strip()
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
                while True:
                    turma_atual = selecionar_turma()

                    if not turma_atual:
                        continue

                    resultado = menu_adm(turma_atual)

                    if resultado == "login":
                        break
                    

            elif tipo == "professor":


                while True:
                    turma_atual = selecionar_turma()

                    if not turma_atual:
                        continue

                    resultado = menu_professor(turma_atual)

                    if resultado == "login":
                        break
                    
             
            
            
        elif escolha == "2":
            print("Programa encerrado")
            break

        else:
            print("Opção inválida")
menus()
