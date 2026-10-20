import json
import os

PRODUTOS_FILE = "data/save/produtos.json"
CONTAS_FILE = "data/save/contas.json"

def garantir_pastas():
    """Garante que a estrutura de pastas existe."""
    os.makedirs("data/save", exist_ok=True)

def salvar_produtos(produtos):
    """Salva a lista de produtos no arquivo JSON."""
    garantir_pastas()
    with open(PRODUTOS_FILE, "w", encoding="utf-8") as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)

def carregar_produtos():
    """Carrega a lista de produtos do arquivo JSON."""
    if os.path.exists(PRODUTOS_FILE):
        with open(PRODUTOS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_contas(contas):
    """Salva a lista de contas no arquivo JSON."""
    garantir_pastas()
    with open(CONTAS_FILE, "w", encoding="utf-8") as f:
        json.dump(contas, f, indent=4, ensure_ascii=False)

def carregar_contas():
    """Carrega a lista de contas do arquivo JSON."""
    if os.path.exists(CONTAS_FILE):
        with open(CONTAS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []