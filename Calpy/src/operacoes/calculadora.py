"""
Calculadora de Operações Matemáticas.

Módulo principal que centraliza todas as operações matemáticas básicas.
"""

from typing import Union
from .adicao import adicao
from .subtracao import subtracao
from .multiplicacao import multiplicacao
from .divisao import divisao
from .fatorial import fatorial
from .potencia import potencia


class Calculadora:
    """
    Classe Calculadora que agrupa todas as operações matemáticas.
    
    Métodos:
        adicionar(a, b): Soma dois números
        subtrair(a, b): Subtrai dois números
        multiplicar(a, b): Multiplica dois números
        dividir(a, b): Divide dois números
        fatorar(n): Calcula o fatorial de um número
        potenciar(base, expoente): Calcula a potência
    """
    
    @staticmethod
    def adicionar(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Soma dois números."""
        return adicao(a, b)
    
    @staticmethod
    def subtrair(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtrai dois números."""
        return subtracao(a, b)
    
    @staticmethod
    def multiplicar(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiplica dois números."""
        return multiplicacao(a, b)
    
    @staticmethod
    def dividir(a: Union[int, float], b: Union[int, float]) -> float:
        """Divide dois números."""
        return divisao(a, b)
    
    @staticmethod
    def fatorar(n: int) -> int:
        """Calcula o fatorial de um número."""
        return fatorial(n)
    
    @staticmethod
    def potenciar(base: Union[int, float], expoente: Union[int, float]) -> Union[int, float]:
        """Calcula a potência (base elevado ao expoente)."""
        return potencia(base, expoente)


# Exemplo de uso
if __name__ == "__main__":
    calc = Calculadora()
    
    print("=== Calculadora de Operações ===")
    print(f"10 + 5 = {calc.adicionar(10, 5)}")
    print(f"10 - 5 = {calc.subtrair(10, 5)}")
    print(f"10 × 5 = {calc.multiplicar(10, 5)}")
    print(f"10 ÷ 5 = {calc.dividir(10, 5)}")
    print(f"5! = {calc.fatorar(5)}")
    print(f"2^8 = {calc.potenciar(2, 8)}")
