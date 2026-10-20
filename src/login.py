import hashlib
from terminal import clear, opcao_invalida, sair
from listas import contas
from banco import salvar_contas

# Função auxiliar para gerar o hash da senha
def gerar_hash(senha):
    # Converte a string para bytes e gera o hash hexadecimal
    return hashlib.sha256(senha.encode('utf-8')).hexdigest()

adm_padrao = "adm"
# O ideal é não deixar a senha do admin exposta no código em texto puro.
# Guardamos direto o hash da senha "1234".
senha_padrao_hash = gerar_hash("1234")

def login():
    while True:
        try:
            clear()
            print("Login\n")

            user_login = input("Usuário: ")
            senha_login = input("Senha: ")
            
            # Criptografa (gera o hash) da senha que o usuário acabou de digitar
            senha_login_hash = gerar_hash(senha_login)

            # verifica admin comparando os hashes
            if user_login == adm_padrao and senha_login_hash == senha_padrao_hash:
                print("\nLogin bem-sucedido!")
                input("Pressione ENTER para continuar...")
                return True

            # verifica contas cadastradas comparando os hashes
            for conta in contas:
                if conta["conta"] == user_login and conta["senha"] == senha_login_hash:
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

        # Criptografa a senha antes de salvar no dicionário e no banco
        senha_hash = gerar_hash(senha)

        conta = {
            "conta": user,
            "senha": senha_hash
        }

        contas.append(conta)
        salvar_contas(conta)

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