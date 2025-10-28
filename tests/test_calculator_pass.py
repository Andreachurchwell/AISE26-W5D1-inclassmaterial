"""
Passing test suite for calculator module
Used to validate that all calculator functions work as expected.
"""
import sys
from pathlib import Path

# Add app directory to path, then import (allow E402 on next import)
sys.path.insert(0, str((Path(__file__).parent.parent / "app").resolve()))

from calculator import (  # noqa: E402
    add,
    subtract,
    multiply,
    divide,
    power,
    modulo,
    square_root,
    absolute,
)


class TestCalculator:
    """Comprehensive tests for calculator functions"""

    def test_addition(self):
        assert add(2, 3) == 5

    def test_subtraction(self):
        assert subtract(5, 3) == 2

    def test_multiplication(self):
        assert multiply(4, 5) == 20

    def test_division(self):
        assert divide(10, 2) == 5

    def test_power(self):
        assert power(2, 3) == 8

    def test_modulo(self):
        assert modulo(9, 4) == 1

    def test_square_root(self):
        assert square_root(25) == 5

    def test_absolute(self):
        assert absolute(-9) == 9
        assert absolute(9) == 9
