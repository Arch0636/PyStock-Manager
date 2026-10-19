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
from src.login import menu_login
from dashboard import dashboard

def main():
    while True:
        logado = menu_login()
        if logado:
            dashboard()

if __name__ == "__main__":
    main()
