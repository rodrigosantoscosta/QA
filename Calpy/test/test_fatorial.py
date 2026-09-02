import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

import pytest
from operacoes.fatorial import fatorial

def test_fatorial_positivo():
    assert fatorial(5) == 120

def test_fatorial_zero():
    assert fatorial(0) == 1

def test_fatorial_maior_que_zero():
    assert fatorial(5) > 0

def test_fatorial_nao_negativo():
    assert not fatorial(5) < 0


def test_fatorial_negativo():
    with pytest.raises(ValueError):
        fatorial(-5)


def test_fatorial_decimal():
    with pytest.raises(TypeError):
        fatorial(3.5)


# ... outros casos de teste