from terminal import clear, opcao_invalida, sair
from listas import contas

adm_padrao = "adm"
senha_padrao = "1234"

def login():
    while True:
        try:
            clear()
            print("Login\n")

            user_login = input("Usuário: ")
            senha_login = input("Senha: ")

            # verifica admin
            if user_login == adm_padrao and senha_login == senha_padrao:
                print("\nLogin bem-sucedido!")
                input("Pressione ENTER para continuar...")
                return True

            # verifica contas cadastradas
            for conta in contas:
                if conta["conta"] == user_login and conta["senha"] == senha_login:
                    print("\nLogin bem-sucedido!")
                    input("Pressione ENTER para continuar...")
                    return True

            clear()
            print("Usuário ou senha incorretos.\n")
            print("1. Tentar novamente")
            print("2. Voltar ao menu\n")

            ten_n = int(input("Escolha uma opção: "))

            if ten_n == 2:
                break

        except ValueError:
            opcao_invalida()


def criar_conta():
    clear()
    print("Cadastro\n")

    try:
        user = input("Escolha o nome de usuário: ")
        senha = input("Escolha a senha: ")

        conta = {
            "conta": user,
            "senha": senha
        }

        contas.append(conta)

        print("\nConta criada com sucesso.")
        input("\nPressione ENTER para continuar...")

    except ValueError:
        opcao_invalida()


def menu_login():
    clear()

    print("1. Entrar")
    print("2. Criar conta")
    print("3. Sair\n")

    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            if login():
                return True

        elif opcao_escolhida == 2:
            criar_conta()

        elif opcao_escolhida == 3:
            clear()
            sair()

        else:
            opcao_invalida()

    except ValueError:
        opcao_invalida()