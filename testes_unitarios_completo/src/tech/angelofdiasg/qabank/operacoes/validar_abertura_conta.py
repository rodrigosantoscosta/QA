def validar_abertura_conta(idade, score_credito, renda_mensal, valor_primeiro_deposito, possui_negativado):
    """
    Regra de negócio (mundo real):
    - Cliente precisa ter pelo menos 18 anos.
    - Score mínimo de 600.
    - Renda mensal deve ser maior que zero.
    - Primeiro depósito precisa ser maior que zero.
    - Se estiver negativado, o sistema pode recusar.
    """
    if idade < 18:
        raise ValueError("Menor de idade não permitido")

    if score_credito < 600:
        return "Recusado"

    if renda_mensal <= 0:
        return "Recusado"

    if valor_primeiro_deposito <= 0:
        return "Recusado"

    return "Aprovado"