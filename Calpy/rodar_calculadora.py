import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from operacoes.calculadora import Calculadora


def main():
    calc = Calculadora()

    print("=== Calculadora ===")
    print(f"10 + 5 = {calc.adicionar(10, 5)}")
    print(f"10 - 5 = {calc.subtrair(10, 5)}")
    print(f"10 * 5 = {calc.multiplicar(10, 5)}")
    print(f"10 / 5 = {calc.dividir(10, 5)}")
    print(f"5! = {calc.fatorar(5)}")
    print(f"2^8 = {calc.potenciar(2, 8)}")


if __name__ == "__main__":
    main()
