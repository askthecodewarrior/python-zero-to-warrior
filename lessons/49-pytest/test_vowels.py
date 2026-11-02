# Practice 2: one answer
from vowels import count_vowels


def test_one_word():
    assert count_vowels("potion") == 3


def test_capitals():
    assert count_vowels("ELIXIR") == 3


def test_no_vowels():
    assert count_vowels("rhythm") == 0
