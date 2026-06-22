from banco import conectar

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
        cursor.close()
        conexao.close()
        return
    
    print(f"\nAlunos da turma {turma}:")

    for aluno in alunos:
        print(f"\nID: {aluno[0]}")
        print(f"Nome: {aluno[1]}")
        print(f"Idade: {aluno[2]}")
        print(f"Turma: {aluno[3]}") 
        print("--------------------")  



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
            print(f"\nID: {aluno[0]}, Nome: {aluno[1]}, Idade: {aluno[2]}, Turma: {aluno[3]}")

            novo_nome = input("\nDigite o novo nome do aluno (deixe em branco caso queira mante-lo): ").strip()

            nova_idade = input("\nDigite a nova idade do aluno (deixe em branco caso queira mante-la): ").strip()
            
            if novo_nome == "":
                novo_nome = aluno[1]

            if nova_idade == "":
                nova_idade = aluno[2]

            
            if not str(novo_nome).replace(" ", "").isalpha():
                print("\nNome inválido\n")

            
            elif not str(nova_idade).isdigit() or int(nova_idade) <= 0:
                print("\nIdade deve ser um número válido\n")

            elif novo_nome == aluno[1] and int(nova_idade) == aluno[2]:
                print("\nNenhuma alteração foi feita\n")

            else:

                print("\n===== ALTERAÇÕES =====")

                if novo_nome != aluno[1]:
                    print(f"Novo nome: {novo_nome}")

                if int(nova_idade) != aluno[2]:
                    print(f"Nova idade: {nova_idade}")

                print()

                confirmacao = input("\nConfirmar alterações? (s/n): ").strip().lower()

                if confirmacao == "s":

                        cursor.execute(
                            "UPDATE alunos SET nome = %s, idade = %s WHERE id_aluno = %s",
                            (novo_nome, int(nova_idade), id_aluno)
                        )
                        
                        conexao.commit()
                
                        print("\nAluno atualizado\n")

                else:
                    print("\nAlteração cancelada\n")
                
        else:
            print("\nAluno não encontrado\n")
            
#
    cursor.close()

    conexao.close()

def excluir_aluno(turma_atual): #ultima parte que eu venécios terei que fazer
    conexao = conectar()

    cursor = conexao.cursor()

    listar_alunos(turma_atual)

    id_aluno = input("digite o ID do aluno que você quer excluir: ").strip()

    if not id_aluno.isdigit():
        print("ID deve ser um número válido\n")

    else:
        cursor.execute("SELECT * FROM alunos WHERE id_aluno = %s AND turma = %s", (id_aluno, turma_atual))

        aluno = cursor.fetchone()



        if aluno:

          
            print("===== DADOS DO ALUNO =====")
          
            print(f"Nome : {aluno[1]}")
            print(f"Idade: {aluno[2]}")
            print(f"Turma: {aluno[3]}\n")
            

            confirmar = input("Deseja realmente excluir este aluno? (s/n): ").strip().lower()

            if confirmar == "s":

                cursor.execute("DELETE FROM alunos WHERE id_aluno = %s AND turma = %s", (id_aluno, turma_atual))

                conexao.commit()

                print("\nAluno excluído\n")

            else:
                print("Exclusão cancelada\n")

        else:
            print("Aluno não encontrado\n")

    cursor.close()

    conexao.close()