# Estrutura do Projeto

## Introdução

Esta secção descreve a **estrutura do projeto**, explicando a organização dos ficheiros e diretórios utilizados na aplicação de gestão desenvolvida em Python.

A organização foi pensada para garantir:
- Clareza na separação de responsabilidades
- Facilidade de manutenção
- Boa leitura do código
- Escalabilidade futura

---

## Visão Geral da Estrutura

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
    ├── visao-geral.md
    ├── estrutura-projeto.md
    ├── categorias.md
    ├── clientes.md
    ├── fornecedores.md
    ├── funcionarios.md
    ├── produtos.md
    └── vendas.md
