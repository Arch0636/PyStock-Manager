from terminal import clear, opcao_invalida, sair
from produtos import adicionar_produtos, listar_produtos

def dashboard():
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
            opcao_invalida()