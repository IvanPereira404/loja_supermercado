"""CRUD para o arquivo `Data/fornecedores.json`.

Fornece funções para carregar, salvar, listar, obter por id, criar,
atualizar e remover fornecedores.


"""
from __future__ import annotations

import json
from pathlib import Path
from typing import List, Dict, Optional, Any
from datetime import datetime


DATA_FILE = Path(__file__).parent / "Data" / "fornecedores.json"


def _ensure_file_exists() -> None:
    """Garante que o arquivo exista e contenha uma lista JSON válida.

    Se o arquivo não existir, cria um com uma lista vazia.
    """
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")


def load_fornecedores() -> List[Dict[str, Any]]:
    """Lê e retorna todas as fornecedores do arquivo.

    Se o arquivo for vazio ou corrompido, reescrevemos um array vazio.
    """
    _ensure_file_exists()
    with DATA_FILE.open("r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            if isinstance(data, list):
                return data
        except json.JSONDecodeError:
            pass
    save_fornecedores([])
    return []


def save_fornecedores(fornecedores: List[Dict[str, Any]]) -> None:
    """Salva a lista de fornecedores no arquivo.

    Substitui o conteúdo do arquivo com a lista fornecida.
    """
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(fornecedores, f, ensure_ascii=False, indent=2)


def _next_id(fornecedores: List[Dict[str, Any]]) -> int:
    """Retorna o próximo ID de fornecedor disponível.

    Busca o maior ID entre as fornecedores e soma 1.
    Se a lista de fornecedores estiver vazia, retorna 1.
    """
    ids = [f.get("id_fornecedor", 0) for f in fornecedores]
    return (max(ids) + 1) if ids else 1


def list_fornecedores() -> List[Dict[str, Any]]:
    """Retorna todas as fornecedores do arquivo.

    Chama `load_fornecedores` e retorna o resultado.
    """
    return load_fornecedores()


def get_fornecedor(id_fornecedor: int) -> Optional[Dict[str, Any]]:
    """Retorna a fornecedora com o ID especificado, ou None se n o existir.

    Procura entre as fornecedores carregadas e retorna a primeira que tiver o ID especificado.
    Se n o encontrar nenhuma, retorna None.
    """
    for f in load_fornecedores():
        if f.get("id_fornecedor") == id_fornecedor:
            return f
    return None


def create_fornecedor(fornecedor: Dict[str, Any]) -> Dict[str, Any]:
    """Cria uma nova fornecedora com os dados fornecidos.

    Os campos "nome" é obrigatório. Os campos "NIF", "telefone", "email" e
    "categoria_fornecida" são opcionais e terão valores padrão se não forem
    fornecidos. O campo "created_at" é setado automaticamente com o valor da
    data atual.

    Retorna a nova fornecedora criada.
    """
    fornecedores = load_fornecedores()
    novo = fornecedor.copy()
    novo_id = _next_id(fornecedores)
    novo["id_fornecedor"] = novo_id
    if "nome" not in novo:
        raise ValueError("Campo 'nome' é obrigatório")
    # campos opcionais padrão
    novo.setdefault("NIF", "")
    novo.setdefault("telefone", "")
    novo.setdefault("email", "")
    novo.setdefault("categoria_fornecida", "")
    novo.setdefault("created_at", datetime.now().isoformat())
    fornecedores.append(novo)
    save_fornecedores(fornecedores)
    return novo


def update_fornecedor(id_fornecedor: int, updates: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Atualiza a fornecedora com `id_fornecedor` usando os dados em `updates`.

    Se `id_fornecedor` for encontrado, atualiza a fornecedora com os dados em `updates`
    e salva as alterações no arquivo. Retorna a fornecedora atualizada.

    Se `id_fornecedor` n o for encontrado, retorna None.
    """
    fornecedores = load_fornecedores()
    for i, f in enumerate(fornecedores):
        if f.get("id_fornecedor") == id_fornecedor:
            updates = {k: v for k, v in updates.items() if k != "id_fornecedor"}
            f.update(updates)
            fornecedores[i] = f
            save_fornecedores(fornecedores)
            return f
    return None


def delete_fornecedor(id_fornecedor: int) -> bool:
    """Remove a fornecedora com o ID especificado.

    Procura entre as fornecedores carregadas e remove a primeira que tiver o ID especificado.
    Se encontrar nenhuma, retorna False.
    Retorna True se a fornecedora for removida com sucesso.
    """
    fornecedores = load_fornecedores()
    for i, f in enumerate(fornecedores):
        if f.get("id_fornecedor") == id_fornecedor:
            fornecedores.pop(i)
            save_fornecedores(fornecedores)
            return True
    return False


def search_fornecedores_by_nome(substr: str) -> List[Dict[str, Any]]:
    """Procura por fornecedores que contenham o substr em seu nome.

    Retorna uma lista de dicionarios com as fornecedores que atendem ao crit rio de busca.
    """
    s = substr.lower()
    return [f for f in load_fornecedores() if s in f.get("nome", "").lower()]


if __name__ == "__main__":
    print("Fornecedores atuais:")
    print(load_fornecedores())

    novo = {
        "nome": "Novo Fornecedor Exemplo",
        "NIF": "000000000",
        "telefone": "(000) 000000000",
        "email": "exemplo@forn.com",
        "categoria_fornecida": "Higiene"
    }
    criado = create_fornecedor(novo)
    print("Fornecedor criado:", criado)
    print("Total agora:", len(load_fornecedores()))

