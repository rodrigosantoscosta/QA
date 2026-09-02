"""
Pacote de operações matemáticas básicas.

Módulos:
    - adicao: Função de adição
    - subtracao: Função de subtração
    - multiplicacao: Função de multiplicação
    - divisao: Função de divisão
    - fatorial: Função de fatorial
    - potencia: Função de potência
"""

from .adicao import adicao
from .subtracao import subtracao
from .multiplicacao import multiplicacao
from .divisao import divisao
from .fatorial import fatorial
from .potencia import potencia

__all__ = [
    'adicao',
    'subtracao',
    'multiplicacao',
    'divisao',
    'fatorial',
    'potencia',
]
