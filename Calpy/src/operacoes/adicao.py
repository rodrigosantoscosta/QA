from typing import Union


def adicao(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Realiza a adição entre dois números.
    
    Args:
        a: Primeiro número (inteiro ou decimal)
        b: Segundo número (inteiro ou decimal)
        
    Returns:
        Union[int, float]: A soma de a e b
        
    Raises:
        TypeError: Se a ou b não forem números
        
    Exemplos:
        >>> adicao(2, 3)
        5
        >>> adicao(2.5, 3.5)
        6.0
        >>> adicao(-5, 10)
        5
    """
    try:
        # Validar tipo
        if not isinstance(a, (int, float)) or isinstance(a, bool):
            raise TypeError(f"Esperado número, recebido {type(a).__name__}")
        if not isinstance(b, (int, float)) or isinstance(b, bool):
            raise TypeError(f"Esperado número, recebido {type(b).__name__}")
        
        # Cálculo
        return a + b
    
    except TypeError:
        raise
