"""CRUD para o arquivo `Data/categorias.json`.

Fornece funções para carregar, salvar, listar, obter por id, criar, atualizar e remover categorias.
Cada categoria tem a estrutura aproximada:

{
	"id_categoria": 1,
	"nome": "Bebidas",
	"descricao": "Água, refrigerantes, sucos e energéticos"
}

"""
from __future__ import annotations

import json
from pathlib import Path
from typing import List, Dict, Optional, Any
from datetime import datetime


DATA_FILE = Path(__file__).parent / "Data" / "categorias.json"


def _ensure_file_exists() -> None:
	DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
	if not DATA_FILE.exists():
		DATA_FILE.write_text("[]", encoding="utf-8")


def load_categorias() -> List[Dict[str, Any]]:
	_ensure_file_exists()
	with DATA_FILE.open("r", encoding="utf-8") as f:
		try:
			data = json.load(f)
			if isinstance(data, list):
				return data
		except json.JSONDecodeError:
			pass
	save_categorias([])
	return []


def save_categorias(categorias: List[Dict[str, Any]]) -> None:
	DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
	with DATA_FILE.open("w", encoding="utf-8") as f:
		json.dump(categorias, f, ensure_ascii=False, indent=2)


def _next_id(categorias: List[Dict[str, Any]]) -> int:
	ids = [c.get("id_categoria", 0) for c in categorias]
	return (max(ids) + 1) if ids else 1


def list_categorias() -> List[Dict[str, Any]]:
	return load_categorias()


def get_categoria(id_categoria: int) -> Optional[Dict[str, Any]]:
	for c in load_categorias():
		if c.get("id_categoria") == id_categoria:
			return c
	return None


def create_categoria(categoria: Dict[str, Any]) -> Dict[str, Any]:
	categorias = load_categorias()
	novo = categoria.copy()
	novo_id = _next_id(categorias)
	novo["id_categoria"] = novo_id
	if "nome" not in novo:
		raise ValueError("Campo 'nome' é obrigatório")
	if "descricao" not in novo:
		novo["descricao"] = ""
	# opcional: adiciona timestamp
	novo.setdefault("created_at", datetime.now().isoformat())
	categorias.append(novo)
	save_categorias(categorias)
	return novo


def update_categoria(id_categoria: int, updates: Dict[str, Any]) -> Optional[Dict[str, Any]]:
	categorias = load_categorias()
	for i, c in enumerate(categorias):
		if c.get("id_categoria") == id_categoria:
			updates = {k: v for k, v in updates.items() if k != "id_categoria"}
			c.update(updates)
			categorias[i] = c
			save_categorias(categorias)
			return c
	return None


def delete_categoria(id_categoria: int) -> bool:
	categorias = load_categorias()
	for i, c in enumerate(categorias):
		if c.get("id_categoria") == id_categoria:
			categorias.pop(i)
			save_categorias(categorias)
			return True
	return False


def search_by_nome(substr: str) -> List[Dict[str, Any]]:
	s = substr.lower()
	return [c for c in load_categorias() if s in c.get("nome", "").lower()]


if __name__ == "__main__":
	print("Categorias atuais:")
	print(load_categorias())

	novo = {"nome": "Higiene", "descricao": "Produtos de higiene pessoal"}
	criado = create_categoria(novo)
	print("Categoria criada:", criado)
	print("Agora há:", len(load_categorias()), "categorias")
