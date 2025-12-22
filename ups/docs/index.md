# Projeto – Aplicação de Gestão em Python

## Visão Geral

Este projeto consiste no desenvolvimento de uma **aplicação de gestão em Python**, executada exclusivamente em **consola**, com persistência de dados em ficheiros **JSON**.  

A aplicação permite a gestão de:
- Clientes
- Fornecedores
- Funcionários
- Produtos
- Categorias
- Vendas

Todas as entidades suportam operações **CRUD** (Create, Read, Update e Delete), conforme solicitado no enunciado do trabalho prático.

O projeto foi desenvolvido seguindo boas práticas de organização, controlo de versões com **Git** e documentação através de **Docusaurus**.

---

## Estrutura do Projeto

A organização do projeto foi pensada para facilitar a manutenção, leitura e escalabilidade do código.

```text
📦 projeto
├── Data/
│   ├── categorias.json
│   ├── clientes.json
│   ├── fornecedores.json
│   ├── funcionarios.json
│   ├── produtos.json
│   └── vendas.json
│
├── crudCategorias.py
├── crudclientes.py
├── crudfornecedores.py
├── crudfuncionarios.py
├── CrudProdutos.py
├── crudvendas.py
│
├── menu.py
├── README.md
├── .gitignore
└── docs/
    ├── index.md
    ├── categorias.md
    ├── clientes.md
    ├── fornecedores.md
    ├── funcionarios.md
    ├── produtos.md
    └── vendas.md
