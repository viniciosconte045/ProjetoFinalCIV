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