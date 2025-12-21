"""CRUD para o arquivo `Data/vendas.json`.

Fornece funções para carregar, salvar, listar, obter por id, criar, atualizar e remover vendas.
Cada venda tem a estrutura aproximada:

{
	"id_venda": 1,
	"data_hora": "2025-12-08T14:30:00",
	"id_cliente": 1,
	"itens": [ {"id_produto": 1001, "quantidade": 2, "preco_unitario": 3.5} ],
	"valor_total": 15.90,
	"forma_pagamento": "cartao_debito"
}

"""
from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional, Any


DATA_FILE = Path(__file__).parent / "Data" / "vendas.json"


def _ensure_file_exists() -> None:
	"""Garante que o arquivo exista e contenha uma lista JSON válida."""
	DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
	if not DATA_FILE.exists():
		DATA_FILE.write_text("[]", encoding="utf-8")


def load_vendas() -> List[Dict[str, Any]]:
	"""Lê e retorna todas as vendas do arquivo."""
	_ensure_file_exists()
	with DATA_FILE.open("r", encoding="utf-8") as f:
		try:
			data = json.load(f)
			if isinstance(data, list):
				return data
		except json.JSONDecodeError:
			pass
	# Se o arquivo estava vazio ou corrompido, reescrevemos um array vazio
	save_vendas([])
	return []


def save_vendas(vendas: List[Dict[str, Any]]) -> None:
	"""Salva a lista de vendas no arquivo JSON de forma legível."""
	DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
	with DATA_FILE.open("w", encoding="utf-8") as f:
		json.dump(vendas, f, ensure_ascii=False, indent=2)


def _next_id(vendas: List[Dict[str, Any]]) -> int:
	ids = [v.get("id_venda", 0) for v in vendas]
	return (max(ids) + 1) if ids else 1


def list_vendas() -> List[Dict[str, Any]]:
	"""Retorna todas as vendas."""
	return load_vendas()


def get_venda(id_venda: int) -> Optional[Dict[str, Any]]:
	"""Retorna a venda com `id_venda` ou None se não existir."""
	for v in load_vendas():
		if v.get("id_venda") == id_venda:
			return v
	return None


def _calcula_valor_total(itens: List[Dict[str, Any]]) -> float:
	total = 0.0
	for it in itens:
		q = float(it.get("quantidade", 0))
		p = float(it.get("preco_unitario", 0))
		total += q * p
	return round(total, 2)


def create_venda(venda: Dict[str, Any]) -> Dict[str, Any]:
	"""Cria uma nova venda, calcula `valor_total` e armazena no arquivo.

	Campos esperados em `venda` (alguns opcionais):
	- id_cliente (recomendado)
	- itens: lista de {id_produto, quantidade, preco_unitario}
	- forma_pagamento (opcional)
	- data_hora (se omitido, usa agora)
	"""
	vendas = load_vendas()
	novo = venda.copy()
	novo_id = _next_id(vendas)
	novo["id_venda"] = novo_id
	if "data_hora" not in novo:
		novo["data_hora"] = datetime.now().isoformat()
	itens = novo.get("itens", [])
	if not isinstance(itens, list):
		raise ValueError("Campo 'itens' deve ser uma lista")
	novo["valor_total"] = _calcula_valor_total(itens)
	vendas.append(novo)
	save_vendas(vendas)
	return novo


def update_venda(id_venda: int, updates: Dict[str, Any]) -> Optional[Dict[str, Any]]:
	"""Atualiza a venda com `id_venda` usando os dados em `updates`.

	Se `itens` for fornecido no updates, recalcula `valor_total`.
	Retorna a venda atualizada ou None se não existir.
	"""
	vendas = load_vendas()
	for i, v in enumerate(vendas):
		if v.get("id_venda") == id_venda:
			# Não permitir alteração de id_venda
			updates = {k: v for k, v in updates.items() if k != "id_venda"}
			v.update(updates)
			if "itens" in updates:
				v["valor_total"] = _calcula_valor_total(v.get("itens", []))
			vendas[i] = v
			save_vendas(vendas)
			return v
	return None


def delete_venda(id_venda: int) -> bool:
	"""Remove a venda com `id_venda`. Retorna True se removida, False caso contrário."""
	vendas = load_vendas()
	for i, v in enumerate(vendas):
		if v.get("id_venda") == id_venda:
			vendas.pop(i)
			save_vendas(vendas)
			return True
	return False


def search_by_cliente(id_cliente: int) -> List[Dict[str, Any]]:
	"""Retorna todas as vendas feitas por um determinado cliente."""
	return [v for v in load_vendas() if v.get("id_cliente") == id_cliente]


if __name__ == "__main__":
	# Exemplo rápido de uso
	print("Lista atual de vendas:")
	print(load_vendas())

	exemplo = {
		"id_cliente": 3,
		"itens": [
			{"id_produto": 1002, "quantidade": 3, "preco_unitario": 2.5},
			{"id_produto": 1003, "quantidade": 1, "preco_unitario": 10.0},
		],
		"forma_pagamento": "dinheiro",
	}

	criado = create_venda(exemplo)
	print("Venda criada:", criado)
	print("Agora há:", len(load_vendas()), "vendas")


