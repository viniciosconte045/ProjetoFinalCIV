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