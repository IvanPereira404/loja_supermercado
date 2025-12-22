# Clientes

## Descrição

O ficheiro `clientes.json` é responsável por armazenar a informação relativa aos **clientes da aplicação**.  
Os dados dos clientes são utilizados principalmente no processo de vendas, permitindo associar cada venda a um cliente específico.

---

## Estrutura do ficheiro

O ficheiro contém uma lista de objetos JSON, onde cada objeto representa um cliente.

### Campos

| Campo | Tipo | Descrição |
|-----|-----|----------|
| `id_cliente` | Inteiro | Identificador único do cliente |
| `nome` | String | Nome completo do cliente |
| `telefone` | String | Contacto telefónico |
| `email` | String | Endereço de email |
| `endereco` | String | Morada do cliente |
| `data_cadastro` | String (YYYY-MM-DD) | Data de registo do cliente |

---

## Exemplo de registo

```json
{
  "id_cliente": 1,
  "nome": "João Silva",
  "telefone": "(11) 99999-8888",
  "email": "joao.silva@email.com",
  "endereco": "Rua A, 123 - São Paulo/SP",
  "data_cadastro": "2024-01-15"
}