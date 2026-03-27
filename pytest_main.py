import pytest
from main import(
    add,
    divide,
    subtract,
    multiply,
)


@pytest.mark.parametrize('a, b, expected', [
    (2, 3, 5),
    (0, 5, 5),
    (3, -5, -2)
])

def test_add_base(a, b, expected):
    assert add(a, b) == expected

def test_add_str():
    with pytest.raises(TypeError):
        add('a', 3)

@pytest.mark.parametrize('a, b, expected', [
    (5, 3, 2),
    (3, 5, -2),
    (3, 0, 3)
])

def test_subtract_base(a, b, expected):
    assert subtract(a, b) == expected

def test_subtract_str():
    with pytest.raises(TypeError):
        subtract('a', 3)

@pytest.mark.parametrize('a, b, expected', [
    (5, 3, 15),
    (3, 0, 0),
    ('a', 3, 'aaa')
])

def test_multiply_base_and_str(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize('a, b, expected', [
    (3, 2, 1.5),
    (0, 5, 0),
])

def test_divide_base(a, b, expected):
    assert divide(a, b) == expected

def test_divide_str():
    with pytest.raises(TypeError):
        divide('a', 5)

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)