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
    produto["validade"] = input("Validade (formato: DD-MM-AAAA): ")

    dados = carregar_dados()
    dados.append(produto)

    salvar_dados(dados)

    print("Produto criado com sucesso!")
    return produto

#read
def listar_produtos():
    dados = carregar_dados()

    return dados

def encontrar_produto():
    dados = carregar_dados()
    
    produto_nome = input("Qual o nome do produto que deseja encontrar?")
    for produto in dados:
        if produto["nome"] == produto_nome:
            return produto

    print("Produto não encontrado.")
    return None

#update
def atualizar_produto():
    dados = carregar_dados()

    produto_nome = input("Qual o nome do produto que deseja atualizar? ")

    for produto in dados:
        if produto["nome"] == produto_nome:
            print("Produto encontrado!")
            print("Dados atuais:", produto)
            
            novo_nome = input(f"Novo nome (atual: {produto['nome']}): ")
            if novo_nome:
                produto["nome"] = novo_nome

            nova_categoria = input(f"Nova categoria (atual: {produto['categoria']}): ")
            if nova_categoria:
                produto["categoria"] = nova_categoria

            novo_preco_custo = input(f"Novo preço de custo (atual: {produto['preco_custo']}): ")
            if novo_preco_custo:
                produto["preco_custo"] = novo_preco_custo

            novo_preco_venda = input(f"Novo preço de venda (atual: {produto['preco_venda']}): ")
            if novo_preco_venda:
                produto["preco_venda"] = novo_preco_venda

            novo_estoque = input(f"Novo estoque (atual: {produto['estoque']}): ")
            if novo_estoque:
                produto["estoque"] = novo_estoque

            novo_codigo_barras = input(f"Novo código de barras (atual: {produto['codigo_barras']}): ")
            if novo_codigo_barras:
                produto["codigo_barras"] = novo_codigo_barras

            nova_validade = input(f"Nova validade (atual: {produto['validade']}): ")
            if nova_validade:
                produto["validade"] = nova_validade

            salvar_dados(dados)

            print("Produto atualizado com sucesso!")
            return produto

    print("Produto não encontrado.")
    return None

#delete
def apagar_produto():
    dados = carregar_dados()

    produto_nome = input("Qual o nome do produto que deseja apagar? ")

    for produto in dados:
        if produto["nome"] == produto_nome:
            dados.remove(produto)

            salvar_dados(dados)

            print("Produto deletado com sucesso!")
            return produto 

    print("Produto não encontrado.")
    return None