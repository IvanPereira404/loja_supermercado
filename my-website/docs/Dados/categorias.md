# Categorias

## Descrição

O ficheiro `categorias.json` é responsável por armazenar as **categorias de produtos** da aplicação.  
As categorias permitem organizar os produtos de forma lógica, facilitando a sua gestão e associação durante as operações de venda.

Este ficheiro é utilizado pelos módulos de gestão de produtos e vendas.

---

## Estrutura do ficheiro

O ficheiro contém uma lista de objetos JSON, onde cada objeto representa uma categoria.

### Campos

| Campo | Tipo | Descrição |
|-----|-----|----------|
| `id_categoria` | Inteiro | Identificador único da categoria |
| `nome` | String | Nome da categoria |
| `descricao` | String | Descrição da categoria |
| `created_at` | String (ISO 8601) | Data de criação da categoria (opcional) |

---

## Exemplo de registo

```json
{
  "id_categoria": 1,
  "nome": "Bebidas",
  "descricao": "Água, refrigerantes, sumos e energéticos"
}