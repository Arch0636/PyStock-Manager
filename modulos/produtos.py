#modulos/produtos.py
import os

class Produto:

    def __init__(self, nome, marca, codigo, validade, quantidade):
        self._nome = nome.title()
        self._marca = marca.upper()
        self._codigo = codigo.upper()
        self._validade = validade
        self._quantidade = quantidade
        
    def __str__(self):
        return (f"{self._nome.ljust(25)} | {self._marca.ljust(25)} | "
                f"{self._codigo.ljust(25)} | {self._validade} | Qtd: {self._quantidade}")

class Estoque:
    produtos_cadastrados = []
    @classmethod
    def adicionar_produto(cls, produto):
        cls.produtos_cadastrados.append(produto)
    
    @classmethod
    def listar_produtos(cls):
        os.system("cls" if os.name == "nt" else "clear")
        print(f'{"Produto".ljust(25)} | {"Marca".ljust(25)} | {"Código".ljust(25)} | {"Validade"} | {"Quantidade"}')
        print("=" * 110)
        
        if not cls.produtos_cadastrados:
            print("Nenhum produto encontrado.")

        else:
            for p in cls.produtos_cadastrados:
                print(p)
                print("-" * 110)

        input("\nPressione ENTER para voltar...")
#            
#class Sistema:
    


# Exemplo de uso:
#p1 = Produto("Arroz", "Tio João", "123456", "10/12/2026", 50)
#p2 = Produto("Feijão", "Camil", "654321", "15/05/2026", 30)

#Estoque.adicionar_produto(p1)
#Estoque.adicionar_produto(p2)

#Estoque.listar_produtos()