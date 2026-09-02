from typing import Union


def multiplicacao(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Realiza a multiplicação entre dois números.
    
    Args:
        a: Primeiro número (multiplicando)
        b: Segundo número (multiplicador)
        
    Returns:
        Union[int, float]: O produto de a e b
        
    Raises:
        TypeError: Se a ou b não forem números
        
    Exemplos:
        >>> multiplicacao(3, 4)
        12
        >>> multiplicacao(2.5, 4)
        10.0
        >>> multiplicacao(-3, 5)
        -15
    """
    try:
        # Validar tipo
        if not isinstance(a, (int, float)) or isinstance(a, bool):
            raise TypeError(f"Esperado número, recebido {type(a).__name__}")
        if not isinstance(b, (int, float)) or isinstance(b, bool):
            raise TypeError(f"Esperado número, recebido {type(b).__name__}")
        
        # Cálculo
        return a * b
    
    except TypeError:
        raise
