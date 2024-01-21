from operators.operatorFunctions import (
    add, sub, mul, div, power, modulo,
    avg, maximum, minimum, neg, factorial, digitAddition
)

import pytest


@pytest.mark.parametrize("operand1, operand2, expected_result", [
    (2, 3, 5),
    (-2, 3, 1),
    (0, 0, 0),
    (5, -2, 3),
    (2, 0, 2)
])
def test_add(operand1, operand2, expected_result):
    assert add(operand1, operand2) == expected_result


@pytest.mark.parametrize("operand1, operand2, expected_result", [
    (5, 3, 2),
    (3, 5, -2),
    (0, 0, 0),
    (-2, -5, 3),
    (0, 2, -2)
])
def test_sub(operand1, operand2, expected_result):
    assert sub(operand1, operand2) == expected_result


@pytest.mark.parametrize("operand1, operand2, expected_result", [
    (2, 3, 6),
    (-2, 3, -6),
    (0, 5, 0),
    (5, -2, -10),
    (2, 0, 0)
])
def test_mul(operand1, operand2, expected_result):
    assert mul(operand1, operand2) == expected_result


@pytest.mark.parametrize("operand1, operand2, expected_result", [
    (6, 3, 2),
    (5, 2, 2.5),
    (0, 5, 0),
    (-10, -2, 5),
    (10, 2, 5)
])
def test_div(operand1, operand2, expected_result):
    if operand2 == 0:
        assert pytest.raises(ZeroDivisionError, div(operand1, operand2))
    else:
        assert div(operand1, operand2) == expected_result


@pytest.mark.parametrize("operand1, operand2, expected_result", [
    (2, 3, 8),
    (-2, 2, 4),
    (3, -1, 1 / 3),
    (-1, 0.5, None),
    (0, 0, None),
    (-8, 3, -512)
])
def test_power(operand1, operand2, expected_result):
    if (operand1 < 0 and (0 < operand2 < 1 or -1 < operand2 < 0)) or (operand1 == 0 and operand2 <= 0):
        with pytest.raises(ArithmeticError):
            power(operand1, operand2)
    else:
        assert power(operand1, operand2) == expected_result


@pytest.mark.parametrize("operand1, operand2, expected_result", [
    (7, 3, 1),
    (5, 2, 1),
    (10, 4, 2),
    (-5, 2, 1),
    (0, 5, 0)
])
def test_modulo(operand1, operand2, expected_result):
    if operand2 == 0:
        pytest.raises(ZeroDivisionError, modulo(operand1, operand2))
    else:
        assert modulo(operand1, operand2) == expected_result


@pytest.mark.parametrize("operand1, operand2, expected_result", [
    (2, 4, 3),
    (0, 0, 0),
    (-2, 2, 0),
    (-3, 5, 1),
    (10, 2, 6)
])
def test_avg(operand1, operand2, expected_result):
    assert avg(operand1, operand2) == expected_result


@pytest.mark.parametrize("operand1, operand2, expected_result", [
    (2, 4, 4),
    (-2, 3, 3),
    (0, 0, 0),
    (5, 2, 5),
    (-5, -2, -2)
])
def test_maximum(operand1, operand2, expected_result):
    assert maximum(operand1, operand2) == expected_result


@pytest.mark.parametrize("operand1, operand2, expected_result", [
    (2, 4, 2),
    (-2, 3, -2),
    (0, 0, 0),
    (5, 2, 2),
    (-5, -2, -5)
])
def test_minimum(operand1, operand2, expected_result):
    assert minimum(operand1, operand2) == expected_result


@pytest.mark.parametrize("operand, expected_result", [
    (5, -5),
    (0, 0),
    (-3, 3),
    (10, -10),
    (-7, 7)
])
def test_neg(operand, expected_result):
    assert neg(operand) == expected_result


@pytest.mark.parametrize("operand, expected_result", [
    (5, 120),
    (0, 1),
    (72.345, None),
    (10, 3628800),
    (10000, float('inf'))
])
def test_factorial(operand, expected_result):
    if operand < 0 or operand != float('inf') and operand % 1 != 0:
        with pytest.raises(ArithmeticError):
            factorial(operand)
    else:
        assert factorial(operand) == expected_result


@pytest.mark.parametrize("operand, expected_result", [
    (123, 6),
    (9876, 30),
    (456, 15),
    (float('inf'), None),
    (999, 27)
])
def test_digitAddition(operand, expected_result):
    if operand < 0 or operand == float('inf'):
        with pytest.raises(ArithmeticError):
            digitAddition(operand)
    else:
        assert digitAddition(operand) == expected_result
