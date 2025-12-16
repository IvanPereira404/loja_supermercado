import json
from datetime import datetime

FICHEIRO = "produtos.json"

def carregar_dados():
    with open(FICHEIRO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_dados(dados):
    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

#create
def criar_produto():
    produto = {}  

    produto["id"] = str(len(carregar_dados()) + 1)
    produto["nome"] = input("Nome do produto: ")
    produto["categoria"] = input("Categoria do produto: ")
    produto["preco_custo"] = input("Preço de custo: ")
    produto["preco_venda"] = input("Preço de venda: ")
    produto["estoque"] = input("Quantidade em estoque: ")
    produto["codigo_barras"] = input("Código de barras: ")
    produto["validade"] = input("Validade (formato: AAAA-MM-DD): ")

    dados = carregar_dados()
    dados.append(produto)

    salvar_dados(dados)

    print("Produto criado com sucesso!")
    return produto

#read
def listar_produtos():
    dados = carregar_dados()

    return dados

def encontra_produto_por_id(produto_id):
    dados = carregar_dados()

    return next((p for p in dados if p["id"] == produto_id), None)

#update
