import pytest

from series.series import fibonacci, lucas, sum_series

def test_fib_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fib_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fib_11():
    actual = fibonacci(11)
    expected = 89
    assert actual == expected

def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_11():
    actual = lucas(11)
    expected = 199
    assert actual == expected

def test_sum_rdm():
    actual = sum_series(4,6,9)
    expected = 39
    assert actual == expected
  
def test_sum_rdm2():
    actual = sum_series(100, 0, 0)
    expected = 0
    assert actual == expected

def test_sum_fib():
    actual = sum_series(5, 0, 1)
    expected = 3
    assert actual == expected

def test_sum_lucas():
    actual = sum_series(5, 2, 1)
    expected = 7
    assert actual == expected
