import json
import os

#conecta este ficheiro ao JSON funcionarios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DADOS = os.path.join(BASE_DIR, "funcionarios.json")

#faz a leitura de dados JSON
def data_read():
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

#Vai buscar o proximo ID de funcionario do ficheiro JSON
def proximo_id(dados):
    ids = [u.get("id_funcionario", 0) for u in dados if isinstance(u, dict)]
    return max(ids, default=0) + 1

#Funcao para criar funcionarios com os parametros e fazendo append para dentro do ficheiro JSON
def create_funcionario(nome, cargo, turno, salario, data_admissao):
    dados = data_read()

    funcionario = {
        "id_funcionario": proximo_id(dados),
        "nome": nome,
        "cargo": cargo,
        "turno": turno,
        "salario": salario,
        "data_admissao": data_admissao
    }

    dados.append(funcionario)
    salvar_dados(dados)


#Funcao que mostra os funcionarios presentes no ficheiro JSON ou mostra que nao ha funcionarios
def read_funcionario():
    dados = data_read()

    if not dados:
        print("Nenhum funcionario encontrado")
        return

    for c in dados:
        print(
            f'ID: {c["id_funcionario"]} | '
            f'Nome: {c["nome"]} | '
            f'Cargo: {c["cargo"]} | '
            f'Turno: {c["turno"]} | '
            f'Salario: {c["salario"]} | '
            f'Data_Admissao: {c["data_admissao"]}'
        )


#Funcao de update atraves do id funcionario selecionado podendo alterar so 1 ou mais campos sem ter de alterar todos
def update_funcionario(id_funcionario, nome=None, cargo=None, turno=None, salario=None, data_admissao=None):
    dados = data_read()

    for c in dados:
        if c.get("id_funcionario") == id_funcionario:
            if nome is not None:
                c["nome"] = nome
            if cargo is not None:
                c["cargo"] = cargo
            if turno is not None:
                c["turno"] = turno
            if salario is not None:
                c["salario"] = salario
            if data_admissao is not None:
                c["data_admissao"] = data_admissao

            salvar_dados(dados)
            print("Funcionario atualizado")
            return

    print("Funcionario não encontrado.")


#Funcao para dar delete do funcionario atravez do id
def delete_funcionario(id_funcionario):
    dados = data_read()
    novos_dados = [c for c in dados if c.get("id_funcionario") != id_funcionario]

    if len(novos_dados) == len(dados):
        print("Funcionario não encontrado")
        return

    salvar_dados(novos_dados)
    print(f"Funcionario ID {id_funcionario} removido")