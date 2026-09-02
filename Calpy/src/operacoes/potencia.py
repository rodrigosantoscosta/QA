from typing import Union


def potencia(base: Union[int, float], expoente: Union[int, float]) -> Union[int, float]:
    """
    Calcula a potência (base elevada ao expoente).
    
    Args:
        base: Número base
        expoente: Número expoente
        
    Returns:
        Union[int, float]: O resultado de base elevado a expoente
        
    Raises:
        TypeError: Se base ou expoente não forem números
        ValueError: Se base for zero e expoente for negativo
        OverflowError: Se o resultado for muito grande
        
    Exemplos:
        >>> potencia(2, 3)
        8
        >>> potencia(5, 2)
        25
        >>> potencia(2, -1)
        0.5
        >>> potencia(9, 0.5)
        3.0
    """
    try:
        # Validar tipo
        if not isinstance(base, (int, float)) or isinstance(base, bool):
            raise TypeError(f"Base deve ser um número, recebido {type(base).__name__}")
        if not isinstance(expoente, (int, float)) or isinstance(expoente, bool):
            raise TypeError(f"Expoente deve ser um número, recebido {type(expoente).__name__}")
        
        # Validar caso especial: 0 elevado a número negativo
        if base == 0 and expoente < 0:
            raise ValueError("Não é possível calcular 0 elevado a um expoente negativo")
        
        # Cálculo
        resultado = base ** expoente
        
        return resultado
    
    except (TypeError, ValueError):
        raise
    except OverflowError as e:
        raise OverflowError("O resultado da potência é muito grande para ser calculado") from e
