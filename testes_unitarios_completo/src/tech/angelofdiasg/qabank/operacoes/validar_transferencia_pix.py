import re


def validar_transferencia_pix(
    saldo_conta,
    valor_transferencia,
    conta_destino,
    limite_diario,
    horario_transferencia
):
    """
    Regra de negócio do QaBank:
    - Saldo da conta deve ser suficiente para a transferência.
    - Valor da transferência deve ser maior que zero.
    - Conta de destino deve ser informada.
    - Transferência não pode exceder o limite diário.
    - Transferência só pode ocorrer em horário comercial (9h às 18h).
    """

    if not conta_destino or conta_destino.strip() == "":
        raise ValueError("Conta de destino não informada")

    if not re.match(r'^[\w.@-]+$', conta_destino):
        raise ValueError("Conta de destino com caracteres inválidos")

    if horario_transferencia < 9 or horario_transferencia > 18:
        raise ValueError("Transferência fora do horário comercial")

    if valor_transferencia <= 0:
        return "Recusado"

    if saldo_conta < valor_transferencia:
        return "Recusado"

    if valor_transferencia > limite_diario:
        return "Recusado"

    return "Aprovado"