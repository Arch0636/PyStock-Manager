"""
Sistema simples de controle de produtos

Projeto educacional em Python com:
- login
- cadastro de contas
- cadastro de produtos
- listagem de produtos
- menu interativo em terminal

Autor: Vinicius Laguardia
"""

import os
import sys

# --------------- configurações ------------------------- #
adm_padrao = "adm"
senha_padrao = "1234"

contas = []
produtos = []


# ------------ funções de produtos ----------------------- #
def listar_produtos():
    clear()

    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("Lista de produtos:\n")

        for i, produto in enumerate(produtos, start=1):
            print(f"{i}. {produto['nome']}")
            print(f"   Código: {produto['codigo']}")
            print(f"   Validade: {produto['validade']}")
            print(f"   Quantidade: {produto['quantidade']}\n")

    input("Pressione ENTER para voltar...")


def adicionar_produtos():
    clear()

    try:
        nome = input("Produto: ")
        codigo_b = int(input("Código de barras: "))
        validade = input("Validade (DD/MM/AAAA): ")
        quantidade = int(input("Quantidade: "))

        novo_produto = {
            "nome": nome,
            "codigo": codigo_b,
            "validade": validade,
            "quantidade": quantidade
        }

        produtos.append(novo_produto)

        print("\nProduto adicionado com sucesso.")
        input("\nPressione ENTER para voltar...")

    except ValueError:
        print("\nErro: insira valores numéricos válidos para código e quantidade.")
        input("\nPressione ENTER para tentar novamente...")


# ------------ dashboard ----------------------- #
def Dashboard():
    while True:
        clear()

        print("1. Adicionar produtos")
        print("2. Listar produtos")
        print("0. Sair")
        print("x. Logout")

        es_d = input("Escolha uma opção: ")

        if es_d == '0':
            clear()
            sair()

        elif es_d == '1':
            adicionar_produtos()

        elif es_d == '2':
            listar_produtos()

        elif es_d == 'x':
            clear()
            break

        else:
            opção_invalida()


# ----------------- funções auxiliares ----------------------- #
def sair():
    print("Encerrando programa...")
    sys.exit()


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def opção_invalida():
    print("\nOpção inválida.")
    input("Pressione ENTER para voltar ao menu...")


# --------------------- funções de login ----------------------------- #
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
        input("\nPressione ENTER para continuar...")

    except ValueError:
        opção_invalida()


def menu_login():
    clear()

    print("1. Entrar")
    print("2. Criar conta")
    print("3. Sair\n")

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
            opção_invalida()

    except ValueError:
        opção_invalida()


def main():
    while True:
        menu_login()


if __name__ == "__main__":
    main()
