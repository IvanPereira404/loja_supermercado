# Funcionários

## Descrição

O ficheiro `funcionarios.json` armazena a informação relativa aos **funcionários da aplicação**.  
Estes dados permitem gerir os colaboradores do sistema, incluindo funções, turnos e informações contratuais.

A gestão de funcionários é importante para o funcionamento interno da aplicação e para a organização do processo de vendas.

---

## Estrutura do ficheiro

O ficheiro contém uma lista de objetos JSON, onde cada objeto representa um funcionário.

### Campos

| Campo | Tipo | Descrição |
|-----|-----|----------|
| `id_funcionario` | Inteiro | Identificador único do funcionário |
| `nome` | String | Nome completo do funcionário |
| `cargo` | String | Função desempenhada |
| `turno` | String | Turno de trabalho (ex: manhã, tarde) |
| `salario` | Decimal | Salário do funcionário |
| `data_admissao` | String (YYYY-MM-DD) | Data de admissão |

---

## Exemplo de registo

```json
{
  "id_funcionario": 201,
  "nome": "Maria Oliveira",
  "cargo": "Atendente",
  "turno": "manha",
  "salario": 1800.0,
  "data_admissao": "2024-03-10"
}