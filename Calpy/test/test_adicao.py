import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

import pytest
from operacoes.adicao import adicao


def test_adicao_positivos():
    assert adicao(2, 3) == 5


def test_adicao_negativos():
    assert adicao(-5, -3) == -8


def test_adicao_misto():
    assert adicao(-5, 10) == 5


def test_adicao_decimais():
    assert adicao(2.5, 3.5) == 6.0


def test_adicao_inteiro_decimal():
    assert adicao(5, 2.3) == 7.3


def test_adicao_zero():
    assert adicao(0, 5) == 5
    assert adicao(5, 0) == 5


def test_adicao_tipo_invalido_string():
    with pytest.raises(TypeError):
        adicao("5", 3)


def test_adicao_tipo_invalido_lista():
    with pytest.raises(TypeError):
        adicao([1, 2], 3)


def test_adicao_tipo_invalido_bool():
    with pytest.raises(TypeError):
        adicao(True, 3)
