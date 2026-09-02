from typing import Union


def fatorial(n: Union[int, float]) -> int:
    """
    Calcula o fatorial de um número inteiro não-negativo.
    
    Args:
        n: Número inteiro não-negativo (0 ou positivo)
        
    Returns:
        int: O fatorial de n
        
    Raises:
        TypeError: Se n não for um número inteiro
        ValueError: Se n for negativo
        OverflowError: Se o resultado for muito grande
        
    Exemplos:
        >>> fatorial(0)
        1
        >>> fatorial(5)
        120
        >>> fatorial(10)
        3628800
    """
    try:
        # Validar tipo
        if not isinstance(n, int):
            raise TypeError(f"Fatorial só é definido para números inteiros, recebido {type(n).__name__}")
        
        # Validar intervalo
        if n < 0:
            raise ValueError(f"Fatorial não definido para números negativos, recebido {n}")
        
        # Caso base
        if n == 0 or n == 1:
            return 1
        
        # Cálculo iterativo
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        
        return resultado
    
    except (TypeError, ValueError):
        # Re-lançar erros de validação
        raise
    except OverflowError as e:
        raise OverflowError(f"Número muito grande para calcular fatorial: {n}") from e
    except Exception as e:
        raise Exception(f"Erro inesperado ao calcular fatorial de {n}: {str(e)}") from e