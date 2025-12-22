# Menu Principal da Aplicação

## Descrição

O ficheiro `menu.py` é o **ponto de entrada principal da aplicação**.  
É responsável por apresentar os menus ao utilizador e encaminhar as opções escolhidas para os respetivos módulos CRUD.

Toda a interação com o sistema é feita através da **consola de texto**, conforme os requisitos do trabalho prático.

---

## Estrutura geral

O menu está organizado de forma hierárquica:

- **Menu Principal**
- Submenus específicos para cada entidade:
  - Clientes
  - Fornecedores
  - Funcionários
  - Produtos
  - Categorias
  - Vendas

Cada submenu permite executar operações CRUD através dos respetivos módulos.

---

## Módulos importados

O `menu.py` integra todos os módulos da aplicação:

- `crudclientes.py`
- `crudfornecedores.py`
- `crudfuncionarios.py`
- `produtos.py`
- `crudcategorias.py`
- `crudvendas.py`

Esta abordagem garante:
- Separação de responsabilidades
- Código modular
- Facilidade de manutenção

---

## Menu Principal

```text
1. Clientes
2. Fornecedores
3. Funcionários
4. Produtos
5. Categorias
6. Vendas