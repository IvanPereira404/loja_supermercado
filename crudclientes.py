import json
import os

#conecta este ficheiro ao JSON clientes
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DADOS = os.path.join(BASE_DIR, "Data/clientes.json")


def data_read():
    """Lê e retorna todos os clientes do arquivo.

    Se o arquivo for vazio ou corrompido, reescrevemos um array vazio.

    Returns:
        lista de clientes (ou [] se o arquivo for vazio ou corrompido)
    """
    if not os.path.exists(DADOS):
        return []

    try:
        with open(DADOS, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []

#Salva os dados no ficheiro JSON
def salvar_dados(dados):
    with open(DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
    print("Dados salvos com sucesso")

#Vai buscar o proximo ID de cliente do ficheiro JSON
def proximo_id(dados):
    ids = [u.get("id_cliente", 0) for u in dados if isinstance(u, dict)]
    return max(ids, default=0) + 1

#Funcao para criar clientes com os parametros e fazendo append para dentro do ficheiro JSON
def create_cliente(nome, telefone, email, endereco, data_cadastro):
    dados = data_read()

    cliente = {
        "id_cliente": proximo_id(dados),
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "endereco": endereco,
        "data_cadastro": data_cadastro
    }

    dados.append(cliente)
    salvar_dados(dados)

#Funcao que mostra os clientes presentes no ficheiro JSON ou mostra que nao ha clientes
def read_clientes():
    dados = data_read()

    if not dados:
        print("Nenhum cliente encontrado")
        return

    for c in dados:
        print(
            f'ID: {c["id_cliente"]} | '
            f'Nome: {c["nome"]} | '
            f'Tel: {c["telefone"]} | '
            f'Email: {c["email"]}'
            f'Endereco: {c["endereco"]}'
            f'Data_Cadastro: {c["data_cadastro"]}'
        )

#Funcao de update atraves do id cliente selecionado podendo alterar so 1 ou mais campos sem ter de alterar todos
def update_cliente(id_cliente, nome=None, telefone=None, email=None, endereco=None, data_cadastro=None):
    dados = data_read()

    for c in dados:
        if c.get("id_cliente") == id_cliente:
            if nome is not None:
                c["nome"] = nome
            if telefone is not None:
                c["telefone"] = telefone
            if email is not None:
                c["email"] = email
            if endereco is not None:
                c["endereco"] = endereco
            if data_cadastro is not None:
                c["data_cadastro"] = data_cadastro

            salvar_dados(dados)
            print("Cliente atualizado")
            return

    print("Cliente não encontrado.")

#Funcao para dar delete do cliente atravez do id
def delete_cliente(id_cliente):
    dados = data_read()
    novos_dados = [c for c in dados if c.get("id_cliente") != id_cliente]

    if len(novos_dados) == len(dados):
        print("Cliente não encontrado")
        return

    salvar_dados(novos_dados)
    print(f"Cliente ID {id_cliente} removido")