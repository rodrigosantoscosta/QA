from typing import Union


def divisao(a: Union[int, float], b: Union[int, float]) -> float:
    """
    Realiza a divisão entre dois números.
    
    Args:
        a: Primeiro número (dividendo)
        b: Segundo número (divisor)
        
    Returns:
        float: O quociente de a por b
        
    Raises:
        TypeError: Se a ou b não forem números
        ZeroDivisionError: Se b for zero
        
    Exemplos:
        >>> divisao(10, 2)
        5.0
        >>> divisao(7, 2)
        3.5
        >>> divisao(-15, 3)
        -5.0
    """
    try:
        # Validar tipo
        if not isinstance(a, (int, float)) or isinstance(a, bool):
            raise TypeError(f"Esperado número, recebido {type(a).__name__}")
        if not isinstance(b, (int, float)) or isinstance(b, bool):
            raise TypeError(f"Esperado número, recebido {type(b).__name__}")
        
        # Validar divisor
        if b == 0:
            raise ZeroDivisionError("Não é possível dividir por zero")
        
        # Cálculo
        return a / b
    
    except (TypeError, ZeroDivisionError):
        raise
