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
	"""Garante que o arquivo existe e contenha uma lista JSON válida.

	Se o arquivo não existir, cria um com uma lista vazia.
	"""
	DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
	if not DATA_FILE.exists():
		DATA_FILE.write_text("[]", encoding="utf-8")


def load_categorias() -> List[Dict[str, Any]]:
	"""Lê e retorna todas as categorias do arquivo.

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
	save_categorias([])
	return []


def save_categorias(categorias: List[Dict[str, Any]]) -> None:
	"""Salva as categorias no arquivo JSON.

	Substitui o conteúdo do arquivo com a lista fornecida.
	"""
	DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
	with DATA_FILE.open("w", encoding="utf-8") as f:
		json.dump(categorias, f, ensure_ascii=False, indent=2)


def _next_id(categorias: List[Dict[str, Any]]) -> int:
	"""Retorna o próximo ID de categoria disponível.

	Retorna o maior ID entre as categorias e soma 1.
	Se a lista de categorias estiver vazia, retorna 1.
	"""
	ids = [c.get("id_categoria", 0) for c in categorias]
	return (max(ids) + 1) if ids else 1


def list_categorias() -> List[Dict[str, Any]]:
	"""Retorna todas as categorias do arquivo.

	Retorna o resultado da chamada `load_categorias()`.
	"""
	return load_categorias()


def get_categoria(id_categoria: int) -> Optional[Dict[str, Any]]:
	"""Retorna a categoria com `id_category` ou None se não existir."""
	for c in load_categorias():
		if c.get("id_categoria") == id_categoria:
			return c
	return None


def create_categoria(categoria: Dict[str, Any]) -> Dict[str, Any]:
	"""Cria uma nova categoria com os dados fornecidos.

	Opcionalmente, pode ser adicionado um timestamp com a data de criação.

	Retorna a nova categoria criada.

	Raises ValueError se o campo "nome" não for fornecido.
	"""
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
	"""Atualiza a categoria com `id_category` usando os dados em `updates`.

	Opcionalmente, pode ser adicionado um timestamp com a data de atualização.

	Retorna a categoria atualizada ou None se não existir.

	Raises ValueError se o campo "nome" não for fornecido.
	"""
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
	"""Remove a categoria com `id_category`.

	Retorna True se a categoria foi removida, False caso contrário.
	"""
	categorias = load_categorias()
	for i, c in enumerate(categorias):
		if c.get("id_categoria") == id_categoria:
			categorias.pop(i)
			save_categorias(categorias)
			return True
	return False


def search_by_nome(substr: str) -> List[Dict[str, Any]]:
	"""Procura por categorias que contenham o substr em seu nome.

	Retorna uma lista de dicionarios com as categorias que atendem ao crit rio de busca.
	"""
	s = substr.lower()
	return [c for c in load_categorias() if s in c.get("nome", "").lower()]


if __name__ == "__main__":
	print("Categorias atuais:")
	print(load_categorias())

	novo = {"nome": "Higiene", "descricao": "Produtos de higiene pessoal"}
	criado = create_categoria(novo)
	print("Categoria criada:", criado)
	print("Agora há:", len(load_categorias()), "categorias")
