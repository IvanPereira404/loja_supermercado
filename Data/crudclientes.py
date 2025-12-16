import json
import os

DADOS = "clientes.json"

def data_read():
    if not os.path.exists(DADOS):
        return []

    try:
        with open(DADOS, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []

def salvar_dados(dados):
    with open(DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
    print("Dados salvos com sucesso")

def proximo_id(dados):
    ids = [u.get("id_cliente", 0) for u in dados if isinstance(u, dict)]
    return max(ids, default=0) + 1

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

def delete_cliente(id_cliente):
    dados = data_read()
    novos_dados = [c for c in dados if c.get("id_cliente") != id_cliente]

    if len(novos_dados) == len(dados):
        print("Cliente não encontrado")
        return

    salvar_dados(novos_dados)
    print(f"Cliente ID {id_cliente} removido")

