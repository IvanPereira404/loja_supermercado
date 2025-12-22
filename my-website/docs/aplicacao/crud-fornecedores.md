# CRUD de Fornecedores

## Descrição

O ficheiro `crudFornecedores.py` implementa as operações **CRUD (Create, Read, Update, Delete)** sobre o ficheiro `fornecedores.json`.

Este módulo é responsável pela gestão dos fornecedores da aplicação, permitindo o registo, consulta, atualização, pesquisa e remoção de fornecedores, com persistência em ficheiro JSON.

---

## Ficheiro de dados associado

- **Caminho:** `Data/fornecedores.json`
- **Formato:** JSON
- **Estrutura:** lista de fornecedores

Exemplo de fornecedor:
```json
{
  "id_fornecedor": 101,
  "nome": "Distribuidora ABC Ltda",
  "NIF": "234567890",
  "telefone": "(351) 919233221",
  "email": "contato@abc.com.pt",
  "categoria_fornecida": "Bebidas"
}