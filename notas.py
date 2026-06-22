from banco import conectar
from alunos import listar_alunos


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


def editar_nota(turma_atual):

    conexao = conectar()

    cursor = conexao.cursor()

    listar_alunos(turma_atual)

    id_aluno = input("Digite o ID do aluno: ").strip()

    if not id_aluno.isdigit():
        print("ID inválido\n")

    else:
         
        cursor.execute(
            "SELECT id_nota, nota FROM notas WHERE id_aluno = %s",
            (id_aluno,)
            )
    
        notas = cursor.fetchall()
    
        if len(notas) == 0:
            print("Nenhuma nota cadastrada para este aluno\n")

        else:
            
            print("===== Notas cadastradas =====")

            for nota in notas:
                print(f"ID da Nota: {nota[0]} - Nota: {nota[1]}")
            
            id_nota = input("Digite o ID da nota que deseja editar: ").strip()

            if not id_nota.isdigit():
                 print("ID da nota inválido\n")
                
                
            else:
                cursor.execute(
                    "SELECT * FROM notas WHERE id_nota = %s and id_aluno = %s",
                    (id_nota, id_aluno)
                )
                nota = cursor.fetchone()

                if not nota:
                    print("Nota não encontrada\n")

                else:

                    nova_nota = input("Digite a nova nota: ").strip().replace(",", ".")

                    if not nova_nota.replace(".", "", 1).isdigit():
                        print("Nota inválida\n")

                    elif float(nova_nota) < 0 or float(nova_nota) > 10:
                        print("A nota deve estar entre 0 e 10\n")

                    else:

                        cursor.execute(
                            "UPDATE notas SET nota = %s WHERE id_nota = %s",
                            (float(nova_nota), id_nota)
                        )

                        conexao.commit()

                        print("\nNota atualizada com sucesso!\n")

    cursor.close()
    conexao.close()


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

def listar_notas(turma_atual):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id_aluno, nome FROM alunos WHERE turma = %s ORDER BY nome",
        (turma_atual,)
    )

    alunos = cursor.fetchall()

    if len(alunos) == 0:
        print("\nNenhum aluno cadastrado\n")

    else:

        print("\n======== LISTA DE NOTAS ========\n")

        for aluno in alunos:

            cursor.execute(
                "SELECT nota FROM notas WHERE id_aluno = %s",
                (aluno[0],)
            )

            notas = cursor.fetchall()

            print(f"Aluno: {aluno[1]}")

            if len(notas) == 0:
                print("Notas: Sem notas cadastradas")

            else:
                lista_notas = [str(nota[0]) for nota in notas]
                print(f"Notas: {', '.join(lista_notas)}")

            print("-----------------------------")

    cursor.close()
    conexao.close()


# mostrar boletim completo
def boletim_geral(turma_atual):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""SELECT id_aluno, nome FROM alunos WHERE turma = %s ORDER BY nome""",
        (turma_atual,))

    alunos = cursor.fetchall()

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado\n")

    else:
        print("\n======== BOLETIM GERAL ========\n")
        soma_medias = 0
        quantidade_alunos = 0
        
        for aluno in alunos:

            cursor.execute(
                "SELECT AVG(nota) FROM notas WHERE id_aluno = %s",
                (aluno[0],)
            )

            media = cursor.fetchone()[0]

            if media is None:
                    media = 0

            soma_medias += media
            quantidade_alunos += 1

            print(f"Aluno: {aluno[1]}")
            print(f"Média: {round(media, 2)}")

            if media >= 7:
                    print("Situacao: Aprovado")

            elif media >= 5:
                    print("Situacao: Recuperacao")

            else:
                print("Situacao: Reprovado")

            print("=========================\n")

            
        media_turma = soma_medias / quantidade_alunos

        print("\n======== MÉDIA GERAL DA TURMA ========")
        print(f"Média da turma: {round(media_turma, 2)}")
        print("======================================\n")

    cursor.close()
    conexao.close()
