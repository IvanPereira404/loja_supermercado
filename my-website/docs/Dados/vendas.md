# Vendas

## Descrição

O ficheiro `vendas.json` armazena a informação relativa às **vendas realizadas na aplicação**.  
Cada venda regista os produtos vendidos, o cliente associado, a forma de pagamento, a data/hora e o valor total da transação.

Este ficheiro é central para o funcionamento da aplicação, pois agrega informação proveniente de vários módulos.

---

## Estrutura do ficheiro

O ficheiro contém uma lista de objetos JSON, onde cada objeto representa uma venda.

### Campos da Venda

| Campo | Tipo | Descrição |
|-----|-----|----------|
| `id_venda` | Inteiro | Identificador único da venda |
| `data_hora` | String (ISO 8601) | Data e hora da venda |
| `id_cliente` | Inteiro | Identificador do cliente |
| `itens` | Lista | Lista de produtos vendidos |
| `valor_total` | Decimal | Valor total da venda |
| `forma_pagamento` | String | Método de pagamento utilizado |

---

### Estrutura dos Itens da Venda

Cada venda contém uma lista de itens com a seguinte estrutura:

| Campo | Tipo | Descrição |
|-----|-----|----------|
| `id_produto` | Inteiro | Identificador do produto |
| `quantidade` | Inteiro | Quantidade vendida |
| `preco_unitario` | Decimal | Preço unitário do produto |

---

## Exemplo de registo

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
  "valor_total": 7.0,
  "forma_pagamento": "cartao_debito"
}