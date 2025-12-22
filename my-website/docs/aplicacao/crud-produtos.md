# CRUD de Produtos

## Descrição

O ficheiro `produtos.py` implementa as operações **CRUD (Create, Read, Update, Delete)** para gestão de produtos no sistema.

Este módulo permite criar, listar, pesquisar, atualizar e remover produtos armazenados no ficheiro `produtos.json`, sendo fortemente integrado com o menu da aplicação e com o módulo de vendas.

---

## Ficheiro de dados associado

- **Caminho:** `Data/produtos.json`
- **Formato:** JSON
- **Estrutura:** lista de produtos

Exemplo de produto:
```json
{
  "id": "1",
  "nome": "Água 1.5L",
  "categoria": "Bebidas",
  "preco_custo": "0.50",
  "preco_venda": "1.00",
  "estoque": "100",
  "codigo_barras": "5601234567890",
  "validade": "31-12-2025"
}