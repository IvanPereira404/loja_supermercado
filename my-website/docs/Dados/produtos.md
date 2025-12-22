# Produtos

## Descrição

O ficheiro `produtos.json` armazena a informação relativa aos **produtos disponíveis na aplicação**.  
Cada produto contém dados essenciais como categoria, preços, stock e código de barras, sendo utilizado nos processos de gestão e venda.

---

## Estrutura do ficheiro

O ficheiro contém uma lista de objetos JSON, onde cada objeto representa um produto.

### Campos

| Campo | Tipo | Descrição |
|-----|-----|----------|
| `id` | String | Identificador único do produto |
| `nome` | String | Nome do produto |
| `categoria` | String | Categoria a que o produto pertence |
| `preco_custo` | Decimal | Preço de custo do produto |
| `preco_venda` | Decimal | Preço de venda ao público |
| `estoque` | Inteiro | Quantidade disponível em stock |
| `codigo_barras` | String | Código de barras do produto |
| `validade` | String | Data de validade do produto |

---

## Exemplo de registo

```json
{
  "id": "1",
  "nome": "skibidi toilet toy",
  "categoria": "brinquedo",
  "preco_custo": "5",
  "preco_venda": "15",
  "estoque": "30",
  "codigo_barras": "123681247",
  "validade": "00-00-0000"
}