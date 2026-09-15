import pytest
from tech.angelofdiasg.qabank.operacoes.validar_transferencia_pix import validar_transferencia_pix

# Parametrize (@pytest.mark.parametrize)
# Data-Driven Testing: tabela de dados com múltiplos cenários.

@pytest.mark.parametrize(
    "saldo_conta, valor_transferencia, conta_destino, limite_diario, horario_transferencia, resultado_esperado",
    [
        # --- Casos básicos ---
        (1000, 500, "123456", 2000, 10, "Aprovado"),
        (500, 500, "123456", 2000, 10, "Aprovado"),
        (10000, 2000, "123456", 2000, 10, "Aprovado"),
        (1000, 500, "123456", 2000, 9, "Aprovado"),
        (1000, 500, "123456", 2000, 18, "Aprovado"),
        (100, 500, "123456", 2000, 10, "Recusado"),
        (1000, 0, "123456", 2000, 10, "Recusado"),
        (1000, -100, "123456", 2000, 10, "Recusado"),
        (10000, 5000, "123456", 2000, 10, "Recusado"),
        # --- Valores extremos ---
        (100, 0.01, "123456", 200, 10, "Aprovado"),
        (99999999, 1000000, "123456", 2000000, 10, "Aprovado"),
        (1, 999999999, "123456", 1000000000, 10, "Recusado"),
        # --- Boundary conditions ---
        (0, 0, "123456", 100, 10, "Recusado"),
        (100, 1, "123456", 0, 10, "Recusado"),
        (-500, 100, "123456", 1000, 10, "Recusado"),
        (500, 100, "123456", 0, 10, "Recusado"),
    ],
    ids=[
        "caminho_feliz",
        "saldo_exato_igual_valor",
        "limite_diario_exato",
        "horario_inicio_comercial",
        "horario_fim_comercial",
        "saldo_insuficiente",
        "valor_zero",
        "valor_negativo",
        "excede_limite_diario",
        "valor_transferencia_1_centavo",
        "transferencia_milhao",
        "valor_gigante_vs_saldo_minimo",
        "saldo_zero_valor_zero",
        "limite_zero_valor_positivo",
        "saldo_negativo_conta_negativada",
        "saldo_positivo_limite_zero",
    ],
)
def test_pix_retornos(
    saldo_conta, valor_transferencia, conta_destino, limite_diario,
    horario_transferencia, resultado_esperado
):
    """Testa cenários que retornam 'Aprovado' ou 'Recusado'."""
    resultado = validar_transferencia_pix(
        saldo_conta, valor_transferencia, conta_destino,
        limite_diario, horario_transferencia
    )
    assert resultado == resultado_esperado


@pytest.mark.parametrize(
    "saldo_conta, valor_transferencia, conta_destino, limite_diario, horario_transferencia",
    [
        # --- Casos básicos ---
        (1000, 500, "", 2000, 10),
        (1000, 500, None, 2000, 10),
        (1000, 500, "123456", 2000, 8),
        (1000, 500, "123456", 2000, 19),
        # --- Caracteres especiais no destino ---
        (1000, 500, "   ", 2000, 10),
        (1000, 500, "!@#$%", 2000, 10),
        (1000, 500, "💀", 2000, 10),
        # --- Horário absurdo ---
        (1000, 500, "123456", 2000, 25),
        (1000, 500, "123456", 2000, -5),
        (1000, 500, "123456", 2000, 99),
        (1000, 500, "123456", 2000, 0),
        # --- Horário fracionário ---
        (1000, 500, "123456", 2000, 8.99),
        (1000, 500, "123456", 2000, 18.01),
    ],
    ids=[
        "conta_destino_vazia",
        "conta_destino_none",
        "horario_antes_comercial",
        "horario_apos_comercial",
        "conta_destino_somente_espacos",
        "conta_destino_caracteres_especiais",
        "conta_destino_emoji",
        "horario_absurdo_25h",
        "horario_negativo",
        "horario_99h",
        "horario_zero_meia_noite",
        "horario_fracionario_antes",
        "horario_fracionario_depois",
    ],
)
def test_pix_excecoes(
    saldo_conta, valor_transferencia, conta_destino, limite_diario,
    horario_transferencia
):
    """Testa cenários de exceção (ValueError) para conta destino e horário."""
    with pytest.raises(ValueError):
        validar_transferencia_pix(
            saldo_conta, valor_transferencia, conta_destino,
            limite_diario, horario_transferencia
        )
