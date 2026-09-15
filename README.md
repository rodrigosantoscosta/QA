# testes_unitarios_completo
Todas as etapas da aula de testes unitários com IA.

## 15/09/2026

### Correção da função `validar_transferencia_pix.py`

- Adicionada validação de `conta_destino` (vazia, nula, só espaços)
- Adicionada validação de `horario_transferencia` (fora do horário comercial 9h–18h)
- Adicionada validação de caracteres inválidos na conta destino (regex)

### Criação de testes unitários com Data-Driven (`test_validar_transferencia_pix.py`)

- 29 cenários de teste using `@pytest.mark.parametrize`
- `test_pix_retornos` — 16 cenários (Aprovado/Recusado)
- `test_pix_excecoes` — 13 cenários (ValueError)
- Cenários absurdos: valores extremos, boundary conditions, horário fracionário, caracteres especiais, emojis

### Atualização do arquivo `cenarios_iniciais.txt`

- Adicionados 29 novos cenários do módulo PIX (cenários 5–33)
- Organização por categorias: básicos, valores extremos, boundary, exceções, horário fracionário

### Implementação com TDD — `validar_solicitacao_emprestimo.py`

- **Ciclo TDD aplicado**: Red (testes falham) → Green (código mínimo) → Refactor
- Função criada com 7 regras de negócio
- Validação de tipos e dados obrigatórios (ValueError)
- `test_validar_solicitacao_emprestimo.py` — 32 cenários com `@pytest.mark.parametrize`
  - `test_emprestimo_retornos` — 20 cenários (Aprovado/Recusado)
  - `test_emprestimo_excecoes` — 12 cenários (ValueError)
