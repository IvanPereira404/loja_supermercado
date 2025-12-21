# Loja de Supermercado

## Descrição

Aplicação em Python para gestão de uma loja de supermercado, desenvolvida inteiramente em consola de texto. O projeto implementa operações CRUD (Create, Read, Update, Delete) para gerenciar produtos e inventário.


## Como Usar

Siga os passos abaixo para executar a aplicação:

1. Abra um terminal na pasta do projeto.
2. Execute o comando:

```bash
python menu.py
```

3. Use as opções do menu para gerir produtos, categorias, clientes, fornecedores, funcionários e vendas.

## Funcionalidades

O projeto inclui um conjunto de funcionalidades para gerir todos os aspetos básicos de uma loja de supermercado:

- **Produtos**
  - Criar, listar, atualizar e eliminar produtos (nome, preço, código, quantidade, categoria).
  - Pesquisar por nome ou filtrar por categoria.
- **Categorias**
  - CRUD completo para categorias de produtos.
- **Clientes**
  - Criar, editar e remover registos de clientes (nome, NIF, morada, contacto).
- **Fornecedores**
  - Gerir fornecedores e os produtos por eles fornecidos.
- **Funcionários**
  - CRUD para dados de funcionários (nome, cargo, contacto).
- **Vendas**
  - Registo de vendas com data, cliente, itens, quantidades e total.
  - Emissão de recibos simples na consola.
- **Inventário & Stock**
  - Atualização automática de stock após vendas.
  - Relatórios de stock baixo e resumos de inventário.
- **Persistência e Backup**
  - Todos os dados são gravados em arquivos JSON na pasta `Data/`.
  - Recomenda-se fazer backups antes de alterações manuais.
- **Interface**
  - Menu interativo em `menu.py` para navegação entre funcionalidades.

> Nota: Se quiser, posso acrescentar exemplos de comandos e capturas de ecrã do menu ao README.

## Estrutura do Projeto

```
loja_supermercado/
├── menu.py
├── produtos.py
├── crudCategorias.py
├── crudclientes.py
├── CrudFornecedores.py
├── crudfuncionarios.py
├── crudvendas.py
├── README.md
└── Data/
    ├── categorias.json
    ├── clientes.json
    ├── fornecedores.json
    ├── funcionarios.json
    ├── produtos.json
    └── vendas.json
```

## Dados

Os dados persistem em arquivos JSON localizados em `Data/`. Cada módulo CRUD lê/escreve no arquivo correspondente (por exemplo, `produtos.py` usa `Data/produtos.json`). Faça backup dos arquivos antes de modificar manualmente.

## Notas de desenvolvimento

- Arquivo principal de execução: `menu.py`.
- Cada módulo CRUD fornece funções para carregar e salvar dados em JSON.
- Se desejar reorganizar o projeto em um pacote (por exemplo, mover os scripts para `app/` e renomear `Data/` para `data/`), posso alterar os imports e atualizar o README.

## Conclusão

Este projeto é uma solução simples para gestão de uma loja de supermercado em linha de comando, utilizando Python e arquivos JSON para armazenamento de dados.

## Desenvolvimento

Projeto desenvolvido como trabalho prático de programação, focado em operações CRUD e manipulação de dados em consola.
