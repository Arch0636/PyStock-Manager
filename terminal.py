import os
import sys

def sair():
    print("Encerrando programa...")
    sys.exit()


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def opcao_invalida():
    print("\nOpção inválida.")
    input("Pressione ENTER para voltar ao menu...")