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
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")


def load_fornecedores() -> List[Dict[str, Any]]:
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
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(fornecedores, f, ensure_ascii=False, indent=2)


def _next_id(fornecedores: List[Dict[str, Any]]) -> int:
    ids = [f.get("id_fornecedor", 0) for f in fornecedores]
    return (max(ids) + 1) if ids else 1


def list_fornecedores() -> List[Dict[str, Any]]:
    return load_fornecedores()


def get_fornecedor(id_fornecedor: int) -> Optional[Dict[str, Any]]:
    for f in load_fornecedores():
        if f.get("id_fornecedor") == id_fornecedor:
            return f
    return None


def create_fornecedor(fornecedor: Dict[str, Any]) -> Dict[str, Any]:
    fornecedores = load_fornecedores()
    novo = fornecedor.copy()
    novo_id = _next_id(fornecedores)
    novo["id_fornecedor"] = novo_id
    if "nome" not in novo:
        raise ValueError("Campo 'nome' é obrigatório")
    # campos opcionais padrão
    novo.setdefault("cnpj", "")
    novo.setdefault("telefone", "")
    novo.setdefault("email", "")
    novo.setdefault("categoria_fornecida", "")
    novo.setdefault("created_at", datetime.now().isoformat())
    fornecedores.append(novo)
    save_fornecedores(fornecedores)
    return novo


def update_fornecedor(id_fornecedor: int, updates: Dict[str, Any]) -> Optional[Dict[str, Any]]:
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
    fornecedores = load_fornecedores()
    for i, f in enumerate(fornecedores):
        if f.get("id_fornecedor") == id_fornecedor:
            fornecedores.pop(i)
            save_fornecedores(fornecedores)
            return True
    return False


def search_fornecedores_by_nome(substr: str) -> List[Dict[str, Any]]:
    s = substr.lower()
    return [f for f in load_fornecedores() if s in f.get("nome", "").lower()]


if __name__ == "__main__":
    print("Fornecedores atuais:")
    print(load_fornecedores())

    novo = {
        "nome": "Novo Fornecedor Exemplo",
        "cnpj": "00.000.000/0001-00",
        "telefone": "(00) 0000-0000",
        "email": "exemplo@forn.com",
        "categoria_fornecida": "Higiene"
    }
    criado = create_fornecedor(novo)
    print("Fornecedor criado:", criado)
    print("Total agora:", len(load_fornecedores()))

