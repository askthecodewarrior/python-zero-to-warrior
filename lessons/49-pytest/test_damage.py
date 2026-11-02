# Practice 1: predict what pytest prints, then run it
from damage import after_hit


def test_small_hit():
    assert after_hit(50, 20) == 30


def test_big_hit():
    assert after_hit(10, 15) == 0
