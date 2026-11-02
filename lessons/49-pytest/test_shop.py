# Tests for the potion shop
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
