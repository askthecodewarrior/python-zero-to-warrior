# Your turn: write a fifth test
# TODO: at the bottom, add a test called test_ten_potions that checks
#       ten potions at 12 gold each: total_cost(12, 10) should be 110
# Run it: pytest -v starter.py (pytest runs a file you name, even one
# that doesn't start with test_). It should say 5 passed.
import pytest
from shop import total_cost


def test_small_order():
    assert total_cost(5, 4) == 20


def test_big_order():
    assert total_cost(30, 5) == 140


def test_exactly_100():
    assert total_cost(25, 4) == 90


def test_zero_potions():
    with pytest.raises(ValueError):
        total_cost(20, 0)
