import json
from datetime import datetime

FICHEIRO = "produtos.json"

def carregar_dados():
    with open(FICHEIRO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_dados(dados):
    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def criar_produto(nome, categoria, preco_custo, preco_venda, estoque, codigo_barras, validade):
    dados = carregar_dados()

    ultimo_id = max([int(p["id"]) for p in dados], default=0)
    novo_id = ultimo_id + 1

    produto = {
        "id": str(novo_id),
        "nome": nome,
        "categoria": categoria,
        "preco_custo": str(preco_custo),
        "preco_venda": str(preco_venda),
        "estoque": str(estoque),
        "codigo_barras": codigo_barras,
        "validade": validade
    }

    dados.append(produto)
    salvar_dados(dados)

    return produto