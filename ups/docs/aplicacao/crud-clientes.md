# CRUD de Clientes

## Descrição

O ficheiro `crudClientes.py` implementa as operações **CRUD (Create, Read, Update, Delete)** sobre o ficheiro `clientes.json`.

Este módulo é responsável pela gestão completa dos clientes da aplicação, incluindo o registo, consulta, atualização e remoção de clientes, com persistência em ficheiro JSON.

---

## Ficheiro de dados associado

- **Nome:** `clientes.json`
- **Localização:** mesmo diretório do módulo
- **Formato:** JSON
- **Estrutura:** lista de clientes

Exemplo de cliente:
```json
{
  "id_cliente": 1,
  "nome": "João Silva",
  "telefone": "(11) 99999-8888",
  "email": "joao@email.com",
  "endereco": "Rua A, 123",
  "data_cadastro": "2024-01-15"
}