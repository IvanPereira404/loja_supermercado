# CRUD de Vendas

## Descrição

O ficheiro `crudVendas.py` implementa as operações **CRUD (Create, Read, Update, Delete)** sobre o ficheiro `vendas.json`.

Este módulo é responsável pelo registo e gestão das vendas realizadas na aplicação, incluindo o cálculo automático do valor total de cada venda.

---

## Ficheiro de dados associado

- **Caminho:** `Data/vendas.json`
- **Formato:** JSON
- **Estrutura:** lista de vendas

Exemplo de venda:
```json
{
  "id_venda": 1,
  "data_hora": "2025-12-08T14:30:00",
  "id_cliente": 1,
  "itens": [
    {
      "id_produto": 1001,
      "quantidade": 2,
      "preco_unitario": 3.5
    }
  ],
  "valor_total": 15.90,
  "forma_pagamento": "cartao_debito"
}