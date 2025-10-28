"""
Initially failing test suite for calculator module
Students will need to fix the calculator to make these tests pass!
"""
import sys
from pathlib import Path

# Add app directory to path, then import (allow E402 on next import)
sys.path.insert(0, str((Path(__file__).parent.parent / "app").resolve()))

from calculator import add, subtract, divide  # noqa: E402


class TestEdgeCases:
    """Test edge cases that will initially fail"""

    def test_add_floats(self):
        result = add(2.5, 3.7)
        assert abs(result - 6.2) < 0.0001

    def test_subtract_floats(self):
        result = subtract(10.5, 3.2)
        assert abs(result - 7.3) < 0.0001

    def test_divide_floats(self):
        result = divide(7, 2)
        assert result == 3.5

    def test_add_large_numbers(self):
        result = add(999_999_999, 1)
        assert result == 1_000_000_000


class TestMissingFunctions:
    """Tests for functions that need to be implemented"""

    def test_square_root(self):
        from calculator import square_root  # noqa: E402
        assert square_root(16) == 4
        assert square_root(25) == 5

    def test_absolute_value(self):
        from calculator import absolute  # noqa: E402
        assert absolute(-5) == 5
        assert absolute(5) == 5
