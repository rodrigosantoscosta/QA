def validar_solicitacao_emprestimo(
    idade,
    score_credito,
    salario_mensal,
    valor_solicitado,
    divida_mensal
):
    """
    Regra de negócio do QaBank:
    - O cliente deve ter pelo menos 18 anos.
    - O score de crédito deve ser maior ou igual a 650.
    - O salário mensal deve ser maior que zero.
    - O valor solicitado deve ser maior que zero.
    - O valor solicitado não pode ultrapassar 10 vezes o salário mensal.
    - A dívida mensal não pode comprometer mais de 40% da renda do cliente.
    """

    # Validação de dados obrigatórios e tipos
    for parametro, valor in [
        ("idade", idade),
        ("score_credito", score_credito),
        ("salario_mensal", salario_mensal),
        ("valor_solicitado", valor_solicitado),
        ("divida_mensal", divida_mensal),
    ]:
        if valor is None:
            raise ValueError(f"{parametro} não pode ser nulo")
        if not isinstance(valor, (int, float)):
            raise ValueError(f"{parametro} deve ser numérico")

    # Menor de idade
    if idade < 18:
        raise ValueError("Menor de idade não permitido")

    # Score insuficiente
    if score_credito < 650:
        return "Recusado"

    # Salário inválido
    if salario_mensal <= 0:
        return "Recusado"

    # Valor do empréstimo inválido
    if valor_solicitado <= 0:
        return "Recusado"

    # Valor acima de 10x o salário
    if valor_solicitado > 10 * salario_mensal:
        return "Recusado"

    # Dívida compromete mais de 40% da renda
    if divida_mensal > 0.4 * salario_mensal:
        return "Recusado"

    return "Aprovado"
