from yatzy import Yatzy
import pytest

def test_write_a_test_first():
    expected = 10
    actual = Yatzy.test(5)
    assert expected == actual

