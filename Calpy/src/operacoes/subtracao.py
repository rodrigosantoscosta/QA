from typing import Union


def subtracao(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Realiza a subtração entre dois números.
    
    Args:
        a: Primeiro número (minuendo)
        b: Segundo número (subtraendo)
        
    Returns:
        Union[int, float]: A diferença de a e b (a - b)
        
    Raises:
        TypeError: Se a ou b não forem números
        
    Exemplos:
        >>> subtracao(10, 3)
        7
        >>> subtracao(5.5, 2.3)
        3.2
        >>> subtracao(-5, 10)
        -15
    """
    try:
        # Validar tipo
        if not isinstance(a, (int, float)) or isinstance(a, bool):
            raise TypeError(f"Esperado número, recebido {type(a).__name__}")
        if not isinstance(b, (int, float)) or isinstance(b, bool):
            raise TypeError(f"Esperado número, recebido {type(b).__name__}")
        
        # Cálculo
        return a - b
    
    except TypeError:
        raise
