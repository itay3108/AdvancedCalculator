import math


def add(operand, operand2):
    """
    Addition method ( + ).
    :param operand: A number
    :param operand2: Another number
    :return: The addition of the two
    """
    return operand + operand2


def sub(operand, operand2):
    """
    Subtraction method ( - ).
    :param operand: A number
    :param operand2: Another number
    :return: The subtraction of the two
    """
    return operand - operand2


def mul(operand, operand2):
    """
    Multiplication method ( * ).
    :param operand: A number
    :param operand2: Another number
    :return: The multiplication of the two
    """
    return operand * operand2


def div(operand, operand2):
    """
    Division method ( / ).
    :param operand: A number
    :param operand2: Another number
    :return: The division of the two
    :raises ZeroDivisionError if the second operand is 0
    """
    if operand2 == 0:
        raise ZeroDivisionError("Can't divide by zero.")
    else:
        return operand / operand2


def power(operand, operand2):
    """
    Power method ( ^ ).
    :param operand: A number
    :param operand2: Another number
    :return: The first operand to the power of the second operand
    """
    if operand <= 0:
        if operand == 0 and operand2 <= 0:
            raise ArithmeticError("Power operation with base 0 requires a positive exponent.")
        elif operand < 0 and (-1 < operand2 < 0 or 0 < operand2 < 1):
            raise ArithmeticError("Power operation with negative base requires a non-fractional exponent.")
    try:
        return math.pow(operand, operand2)
    except OverflowError:
        return float('inf')


def modulo(operand, operand2):
    """
    Modulo method ( % ).
    :param operand: A number
    :param operand2: Another number
    :return: The modulo of the two
    :raises ZeroDivisionError if the second operand is 0
    """
    if operand2 == 0:
        raise ZeroDivisionError("Math Error: Can't have the remaining of a division by zero.")
    return operand % operand2


def avg(operand, operand2):
    """
    Average method ( @ ).
    :param operand: A number
    :param operand2: Another number
    :return: The average of the two
    """
    return (operand + operand2) / 2


def maximum(operand, operand2):
    """
    Maximum method ( $ ).
    :param operand: A number
    :param operand2: Another number
    :return: The larger number from the two
    """
    return max(operand, operand2)


def minimum(operand, operand2):
    """
    Minimum method ( & ).
    :param operand: A number
    :param operand2: Another number
    :return: The smaller number from the two
    """
    return min(operand, operand2)


def neg(operand):
    """
    Negative method ( ~ ).
    :param operand: A number
    :return: The negative form of the number
    """
    return -operand


def factorial(operand):
    """
    Factorial method ( ! ).
    :param operand: A number
    :return: All the whole numbers from 1 to operand multiplied
    :raises ArithmeticError if the number is negative or a fractional number
    """
    infReached = False
    if operand >= 0:
        try:
            if operand % 1 == 0:
                result = 1.0
                i = 2
                while not infReached and i < operand + 1:
                    result *= i
                    if result == float('inf'):
                        infReached = True
                    i += 1
                return result
            else:
                raise ArithmeticError("Math Error: Can't activate a factorial method on a fractional number.")
        except (ValueError, ArithmeticError):
            if operand == float('inf'):
                return float('inf')
            raise ArithmeticError("Math Error: Can't activate a factorial method on a fractional number.")
    else:
        raise ArithmeticError("Math Error: Can't activate a factorial method on a negative number.")


def digitAddition(operand):
    """
    Digit addition method ( # ).
    :param operand: A number
    :return: Sum of the digits in the number
    :raises ArithmeticError if the number is negative or inf
    """
    if operand >= 0:
        if operand == float('inf'):
            raise ArithmeticError("Math Error: Can't activate the digit addition on an infinite number.")
        dividedOp = str(operand)
        dividedOp = list(dividedOp)
        return sum(float(char) for char in dividedOp if char.isnumeric())
    else:
        raise ArithmeticError("Math Error: Can't activate the digit addition on a negative number.")
