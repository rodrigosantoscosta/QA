import pytest
from tech.angelofdiasg.qabank.operacoes.validar_solicitacao_emprestimo import validar_solicitacao_emprestimo

# TDD - Data-Driven Testing (@pytest.mark.parametrize)

# ==============================
# Retornos: "Aprovado" ou "Recusado"
# ==============================

@pytest.mark.parametrize(
    "idade, score_credito, salario_mensal, valor_solicitado, divida_mensal, resultado_esperado",
    [
        # --- Casos básicos ---
        (30, 700, 5000, 10000, 1000, "Aprovado"),
        (18, 650, 3000, 5000, 500, "Aprovado"),
        (25, 800, 10000, 50000, 2000, "Aprovado"),
        # --- Score ---
        (30, 649, 5000, 10000, 1000, "Recusado"),
        (30, 500, 5000, 10000, 1000, "Recusado"),
        # --- Salário ---
        (30, 700, 0, 10000, 1000, "Recusado"),
        (30, 700, -1000, 10000, 1000, "Recusado"),
        # --- Valor solicitado ---
        (30, 700, 5000, 0, 1000, "Recusado"),
        (30, 700, 5000, -5000, 1000, "Recusado"),
        # --- Valor > 10x salário ---
        (30, 700, 5000, 50001, 1000, "Recusado"),
        (30, 700, 5000, 100000, 1000, "Recusado"),
        # --- Dívida > 40% da renda ---
        (30, 700, 5000, 10000, 2001, "Recusado"),
        (30, 700, 5000, 10000, 5000, "Recusado"),
        # --- Boundary conditions ---
        (18, 650, 3000, 30000, 1199, "Aprovado"),
        (30, 700, 5000, 50000, 2000, "Aprovado"),
        (30, 650, 1, 10, 0, "Aprovado"),
        (30, 700, 5000, 50001, 0, "Recusado"),
        (30, 700, 5000, 10000, 2000, "Aprovado"),
        # --- Valores extremos ---
        (30, 700, 999999, 9999990, 0, "Aprovado"),
        (30, 700, 1, 10, 0, "Aprovado"),
    ],
    ids=[
        "caminho_feliz_30_700",
        "caminho_feliz_18_650",
        "caminho_feliz_25_800",
        "score_abaixo_limite",
        "score_muito_baixo",
        "salario_zero",
        "salario_negativo",
        "valor_zero",
        "valor_negativo",
        "valor_acima_10x_salario",
        "valor_muito_acima_10x",
        "divida_acima_40_pct",
        "divida_muito_acima_40_pct",
        "boundary_idade_18_score_650",
        "boundary_valor_exato_10x",
        "boundary_salario_minimo",
        "boundary_valor_acima_10x",
        "boundary_divida_exato_40_pct",
        "valores_extremos_altos",
        "valores_extremos_baixos",
    ],
)
def test_emprestimo_retornos(
    idade, score_credito, salario_mensal, valor_solicitado,
    divida_mensal, resultado_esperado
):
    """Testa cenários que retornam 'Aprovado' ou 'Recusado'."""
    resultado = validar_solicitacao_emprestimo(
        idade, score_credito, salario_mensal, valor_solicitado, divida_mensal
    )
    assert resultado == resultado_esperado


# ==============================
# Exceções: ValueError
# ==============================

@pytest.mark.parametrize(
    "idade, score_credito, salario_mensal, valor_solicitado, divida_mensal",
    [
        # --- Menor de idade ---
        (17, 700, 5000, 10000, 1000),
        (10, 800, 3000, 5000, 500),
        (0, 700, 5000, 10000, 1000),
        # --- Dados None ---
        (None, 700, 5000, 10000, 1000),
        (30, None, 5000, 10000, 1000),
        (30, 700, None, 10000, 1000),
        (30, 700, 5000, None, 1000),
        (30, 700, 5000, 10000, None),
        # --- Tipos inválidos ---
        (30, "abc", 5000, 10000, 1000),
        (30, 700, "abc", 10000, 1000),
        (30, 700, 5000, "abc", 1000),
        (30, 700, 5000, 10000, "abc"),
    ],
    ids=[
        "menor_17",
        "menor_10",
        "menor_0",
        "idade_none",
        "score_none",
        "salario_none",
        "valor_none",
        "divida_none",
        "score_tipo_invalido",
        "salario_tipo_invalido",
        "valor_tipo_invalido",
        "divida_tipo_invalido",
    ],
)
def test_emprestimo_excecoes(
    idade, score_credito, salario_mensal, valor_solicitado, divida_mensal
):
    """Testa cenários de exceção (ValueError) para idade e dados inválidos."""
    with pytest.raises(ValueError):
        validar_solicitacao_emprestimo(
            idade, score_credito, salario_mensal, valor_solicitado, divida_mensal
        )
