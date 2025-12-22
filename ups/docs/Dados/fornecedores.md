# Fornecedores

## Descrição

O ficheiro `fornecedores.json` armazena a informação relativa aos **fornecedores da aplicação**.  
Os fornecedores são responsáveis pelo fornecimento de produtos, estando normalmente associados a uma ou mais categorias.

Esta informação é essencial para a gestão de produtos e para o controlo da origem dos mesmos.

---

## Estrutura do ficheiro

O ficheiro contém uma lista de objetos JSON, onde cada objeto representa um fornecedor.

### Campos

| Campo | Tipo | Descrição |
|-----|-----|----------|
| `id_fornecedor` | Inteiro | Identificador único do fornecedor |
| `nome` | String | Nome da empresa fornecedora |
| `NIF` | String | Número de Identificação Fiscal |
| `telefone` | String | Contacto telefónico |
| `email` | String | Endereço de email |
| `categoria_fornecida` | String | Categoria de produtos fornecida |

---

## Exemplo de registo

```json
{
  "id_fornecedor": 101,
  "nome": "Distribuidora ABC Ltda",
  "NIF": "234567890",
  "telefone": "(351) 919233221",
  "email": "contato@abc.com.pt",
  "categoria_fornecida": "Bebidas"
}