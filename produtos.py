from listas import produtos
from terminal import clear

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