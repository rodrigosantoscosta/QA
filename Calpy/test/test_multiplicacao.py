import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

import pytest
from operacoes.multiplicacao import multiplicacao


def test_multiplicacao_positivos():
    assert multiplicacao(3, 4) == 12


def test_multiplicacao_negativos():
    assert multiplicacao(-3, -4) == 12


def test_multiplicacao_misto():
    assert multiplicacao(-3, 5) == -15


def test_multiplicacao_decimais():
    assert multiplicacao(2.5, 4) == 10.0


def test_multiplicacao_decimal_decimal():
    assert multiplicacao(2.5, 1.5) == pytest.approx(3.75)


def test_multiplicacao_zero():
    assert multiplicacao(0, 5) == 0
    assert multiplicacao(5, 0) == 0


def test_multiplicacao_um():
    assert multiplicacao(5, 1) == 5
    assert multiplicacao(1, 5) == 5


def test_multiplicacao_tipo_invalido_string():
    with pytest.raises(TypeError):
        multiplicacao("3", 4)


def test_multiplicacao_tipo_invalido_lista():
    with pytest.raises(TypeError):
        multiplicacao([1, 2], 3)


def test_multiplicacao_tipo_invalido_bool():
    with pytest.raises(TypeError):
        multiplicacao(True, 3)
