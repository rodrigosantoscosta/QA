import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

import pytest
from operacoes.subtracao import subtracao


def test_subtracao_positivos():
    assert subtracao(10, 3) == 7


def test_subtracao_negativos():
    assert subtracao(-5, -3) == -2


def test_subtracao_misto():
    assert subtracao(-5, 10) == -15


def test_subtracao_decimais():
    assert subtracao(5.5, 2.3) == pytest.approx(3.2)


def test_subtracao_inteiro_decimal():
    assert subtracao(10, 2.5) == 7.5


def test_subtracao_zero():
    assert subtracao(0, 5) == -5
    assert subtracao(5, 0) == 5


def test_subtracao_numero_consigo_mesmo():
    assert subtracao(10, 10) == 0


def test_subtracao_tipo_invalido_string():
    with pytest.raises(TypeError):
        subtracao("10", 3)


def test_subtracao_tipo_invalido_lista():
    with pytest.raises(TypeError):
        subtracao([1, 2], 3)


def test_subtracao_tipo_invalido_bool():
    with pytest.raises(TypeError):
        subtracao(True, 3)
