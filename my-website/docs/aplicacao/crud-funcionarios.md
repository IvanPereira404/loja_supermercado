# CRUD de Funcionários

## Descrição

O ficheiro `crudFuncionarios.py` implementa as operações **CRUD (Create, Read, Update, Delete)** sobre o ficheiro `funcionarios.json`.

Este módulo é responsável pela gestão dos funcionários da aplicação, permitindo o registo, consulta, atualização e remoção de colaboradores, com persistência em ficheiro JSON.

---

## Ficheiro de dados associado

- **Nome:** `funcionarios.json`
- **Localização:** mesmo diretório do módulo
- **Formato:** JSON
- **Estrutura:** lista de funcionários

Exemplo de funcionário:
```json
{
  "id_funcionario": 201,
  "nome": "Maria Oliveira",
  "cargo": "Atendente",
  "turno": "manha",
  "salario": 1800.0,
  "data_admissao": "2024-03-10"
}