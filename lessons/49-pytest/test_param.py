# Practice 3: one answer (the four totals in one test)
import pytest
from shop import total_cost


@pytest.mark.parametrize("price, count, expected", [
    (5, 4, 20),
    (30, 5, 140),
    (25, 4, 90),
    (12, 10, 110),
])
def test_total_cost(price, count, expected):
    assert total_cost(price, count) == expected
