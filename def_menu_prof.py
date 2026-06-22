def menu_prof(turma_atual):

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
            print(listar_notas(turma_atual))

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
        