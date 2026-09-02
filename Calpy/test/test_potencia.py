import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

import pytest
from operacoes.potencia import potencia


def test_potencia_positiva():
    assert potencia(2, 3) == 8


def test_potencia_quadrado():
    assert potencia(5, 2) == 25


def test_potencia_zero_expoente():
    assert potencia(5, 0) == 1


def test_potencia_base_um():
    assert potencia(1, 10) == 1


def test_potencia_expoente_um():
    assert potencia(5, 1) == 5


def test_potencia_expoente_negativo():
    assert potencia(2, -1) == 0.5


def test_potencia_raiz_quadrada():
    assert potencia(9, 0.5) == 3.0


def test_potencia_raiz_cubica():
    assert potencia(8, 1/3) == pytest.approx(2.0)


def test_potencia_base_negativa():
    assert potencia(-2, 3) == -8


def test_potencia_base_negativa_expoente_par():
    assert potencia(-2, 2) == 4


def test_potencia_decimais():
    assert potencia(2.5, 2) == pytest.approx(6.25)


def test_potencia_zero_elevado_a_positivo():
    assert potencia(0, 5) == 0


def test_potencia_zero_elevado_a_zero():
    assert potencia(0, 0) == 1


def test_potencia_zero_elevado_a_negativo():
    with pytest.raises(ValueError):
        potencia(0, -5)


def test_potencia_tipo_invalido_base_string():
    with pytest.raises(TypeError):
        potencia("2", 3)


def test_potencia_tipo_invalido_expoente_string():
    with pytest.raises(TypeError):
        potencia(2, "3")


def test_potencia_tipo_invalido_bool_base():
    with pytest.raises(TypeError):
        potencia(True, 3)
