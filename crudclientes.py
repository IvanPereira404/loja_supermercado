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


def salvar_dados(dados):
    """Salva os dados no ficheiro JSON.

    Args:
        dados (list): lista de clientes em formato de dicionário

    Returns:
        None
    """
    with open(DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
    print("Dados salvos com sucesso")

#Vai buscar o proximo ID de cliente do ficheiro JSON
def proximo_id(dados):
    ids = [u.get("id_cliente", 0) for u in dados if isinstance(u, dict)]
    return max(ids, default=0) + 1

def create_cliente(nome, telefone, email, endereco, data_cadastro):
    """Cria um novo cliente e o adiciona ao ficheiro JSON.

    Args:
        nome (str): Nome do cliente.
        telefone (str): Telefone do cliente.
        email (str): Email do cliente.
        endereco (str): Endereço do cliente.
        data_cadastro (str): Data de cadastro do cliente (formato livre).

    Returns:
        None
    """
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
    """Mostra todos os clientes presentes no ficheiro JSON.

    Se o ficheiro estiver vazio, mostra uma mensagem informando que
    nenhum cliente foi encontrado.

    """
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
    """Atualiza campos de um cliente identificado pelo seu ID.

    Parâmetros opcionais com valor None são ignorados (não alteram o campo).
    Imprime mensagem se o cliente for atualizado ou se não for encontrado.
    """
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
    """Remove um cliente identificado pelo seu ID.

    Procura o cliente na lista persistida e, se encontrado,
    remove-o e salva os dados atualizados.
    Imprime mensagem se o cliente for atualizado ou se não for encontrado.
    """
    dados = data_read()
    novos_dados = [c for c in dados if c.get("id_cliente") != id_cliente]

    if len(novos_dados) == len(dados):
        print("Cliente não encontrado")
        return

    salvar_dados(novos_dados)
    print(f"Cliente ID {id_cliente} removido")