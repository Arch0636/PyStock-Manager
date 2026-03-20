import os
import sys

# --------------- configurações ------------------------- #
adm_padrao = "adm"
senha_padrao = "1234"

contas = []
produtos = []


# ------------ programa principal ----------------------- #
def listar_produtos():
    pass

def adicionar_produtos():
    clear()
    try:
        nome = input("Produto: ")
        codigo_b = int(input("código de barras: "))
        validade = input("Validade (DD/MM/AAAA): ")
        quantidade = int(input("quantidade: "))

        novo_produto = {
            "nome": nome,
            "codigo": codigo_b,
            "validade": validade,
            "quantidade": quantidade
        }

        produtos.append(novo_produto)

        print("Produto adicionado com sucesso.")
        input("\nPressione Enter para voltar...")

    except ValueError:
        print("\nErro: Insira valores numéricos válidos para código e quantidade.")
        input("\nPressione Enter para tentar novamente...")


def Dashboard():
    while True:
        clear()

        print("1. adicionar produtos")
        print("0. Sair")
        print("x. Logout")

        es_d = input("Escolha uma opção: ")

        if es_d == '0':
            clear()
            sair()

        elif es_d == '1':
            adicionar_produtos()

        elif es_d == 'x':
            clear()
            break

        else:
            print("Opção inválida\n")


# ----------------- funções auxiliares ----------------------- #
def sair():
    print("Encerrando Programa...")
    sys.exit()


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def opção_invalida():
    print("Opção inválida\n")
    input("Clique em uma tecla para voltar ao menu principal")
    clear()


# --------------------- Funções de login ----------------------------- #
def login():
    while True:
        try:
            clear()
            print("Login\n")

            user_login = input("Usuário: ")
            senha_login = input("Senha: ")

            # verifica admin
            if user_login == adm_padrao and senha_login == senha_padrao:
                print("Login bem-sucedido!")
                return True

            # verifica contas cadastradas
            for conta in contas:
                if conta["conta"] == user_login and conta["senha"] == senha_login:
                    print("Login bem-sucedido!")
                    return True

            clear()
            print("Usuário ou senha incorretos.\n")
            print("1 tentar novamente.")
            print("2 Voltar ao menu.\n")

            ten_n = int(input("Escolha uma opção: "))

            if ten_n == 2:
                break

        except ValueError:
            opção_invalida()


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
        input("\nPressione ENTER para continuar")

    except ValueError:
        pass


def menu_login():
    clear()

    print("1 Entrar")
    print("2 Criar conta")
    print("3 sair\n")

    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            if login():
                Dashboard()

        elif opcao_escolhida == 2:
            criar_conta()

        elif opcao_escolhida == 3:
            clear()
            sair()

        else:
            print("Opção inválida.")

    except ValueError:
        opção_invalida()


def main():
    while True:
        menu_login()


if __name__ == "__main__":
    main()