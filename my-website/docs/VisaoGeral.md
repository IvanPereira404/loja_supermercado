# Visão Geral

## Introdução

Este projeto consiste no desenvolvimento de uma **aplicação de gestão em Python**, executada exclusivamente em **modo consola**, com persistência de dados em ficheiros **JSON**.

A aplicação foi desenvolvida no âmbito de um **trabalho prático académico**, tendo como principal objetivo aplicar conceitos de programação, organização de projetos, controlo de versões com Git e documentação técnica.

---

## Objetivos do Projeto

Os principais objetivos do projeto são:

- Desenvolver uma aplicação funcional em Python
- Implementar operações **CRUD** (Create, Read, Update, Delete)
- Utilizar ficheiros JSON para armazenamento de dados
- Organizar o código de forma modular
- Aplicar boas práticas de controlo de versões com Git
- Criar documentação clara e acessível utilizando Markdown e Docusaurus

---

## Descrição da Aplicação

A aplicação permite a gestão de diferentes entidades fundamentais para o funcionamento de um sistema comercial, nomeadamente:

- **Clientes** – gestão de dados pessoais e histórico
- **Fornecedores** – gestão de entidades fornecedoras
- **Funcionários** – gestão de recursos humanos
- **Produtos** – gestão de stock e preços
- **Categorias** – classificação de produtos
- **Vendas** – registo e consulta de vendas realizadas

Cada entidade possui um módulo próprio responsável pelas operações CRUD, garantindo separação de responsabilidades e facilidade de manutenção.

---

## Funcionamento Geral

A interação com o utilizador é feita através de um **menu em consola**, que permite navegar entre os diferentes módulos da aplicação.

O fluxo geral de funcionamento é o seguinte:

1. O utilizador executa o ficheiro `menu.py`
2. É apresentado um menu principal com as várias opções
3. O utilizador seleciona a entidade a gerir
4. São executadas operações CRUD conforme a opção escolhida
5. Os dados são guardados automaticamente em ficheiros JSON

---

## Persistência de Dados

A persistência de dados é assegurada através de ficheiros **JSON**, localizados na pasta `Data/`.

Esta abordagem permite:
- Simplicidade na leitura e escrita de dados
- Facilidade de manutenção
- Independência de bases de dados externas

---

## Organização do Projeto

O projeto encontra-se organizado de forma modular, separando:

- Lógica da aplicação
- Gestão de dados
- Interface com o utilizador
- Documentação

Esta estrutura facilita a leitura do código, a manutenção e futuras extensões da aplicação.

---

## Conclusão

Este projeto demonstra a aplicação prática dos conhecimentos adquiridos ao longo da unidade curricular, nomeadamente no desenvolvimento de aplicações em Python, utilização de ficheiros JSON, controlo de versões com Git e criação de documentação técnica.

A aplicação encontra-se funcional, organizada e preparada para possíveis melhorias futuras.
