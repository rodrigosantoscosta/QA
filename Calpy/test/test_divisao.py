import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

import pytest
from operacoes.divisao import divisao


def test_divisao_positivos():
    assert divisao(10, 2) == 5.0


def test_divisao_resultado_decimal():
    assert divisao(7, 2) == 3.5


def test_divisao_negativos():
    assert divisao(-15, 3) == -5.0


def test_divisao_misto():
    assert divisao(-10, 2) == -5.0


def test_divisao_decimais():
    assert divisao(10.0, 2.0) == 5.0


def test_divisao_numero_por_um():
    assert divisao(5, 1) == 5.0


def test_divisao_zero_por_numero():
    assert divisao(0, 5) == 0.0


def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        divisao(10, 0)


def test_divisao_tipo_invalido_string():
    with pytest.raises(TypeError):
        divisao("10", 2)


def test_divisao_tipo_invalido_lista():
    with pytest.raises(TypeError):
        divisao([1, 2], 2)


def test_divisao_tipo_invalido_bool():
    with pytest.raises(TypeError):
        divisao(True, 2)
