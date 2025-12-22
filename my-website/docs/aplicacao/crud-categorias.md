# CRUD de Categorias

## Descrição

O ficheiro `crudCategorias.py` implementa todas as operações **CRUD (Create, Read, Update, Delete)** sobre o ficheiro `categorias.json`.

Este módulo é responsável por:
- Garantir a existência do ficheiro de dados
- Ler e escrever categorias em formato JSON
- Gerir identificadores únicos
- Validar dados de entrada
- Fornecer funções reutilizáveis para o menu principal

---

## Ficheiro de dados associado

- **Caminho:** `Data/categorias.json`
- **Formato:** JSON
- **Estrutura:** lista de categorias

Exemplo de categoria:
```json
{
  "id_categoria": 1,
  "nome": "Bebidas",
  "descricao": "Água, refrigerantes, sucos e energéticos"
}