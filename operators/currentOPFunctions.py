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
        raise ZeroDivisionError("You can't divide by zero.")
    else:
        return operand / operand2


def power(operand, operand2):
    """
    Power method ( ^ ).
    :param operand: A number
    :param operand2: Another number
    :return: The first operand to the power of the second operand
    """
    return operand ** operand2


def modulo(operand, operand2):
    """
    Modulo method ( % ).
    :param operand: A number
    :param operand2: Another number
    :return: The modulo of the two
    :raises ZeroDivisionError if the second operand is 0
    """
    if operand2 == 0:
        raise ZeroDivisionError("You can't have the remaining of a division by zero.")
    return operand % operand2


def avg(operand, operand2):
    """
    Average method ( @ ).
    :param operand: A number
    :param operand2: Another number
    :return: The average of the two
    """
    return (operand + operand2)/2


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
    :return: all the whole numbers from 1 to operand multiplied
    :raises ArithmeticError if the number is negative or a fractional number
    """
    if operand > 0:
        if isinstance(operand, int):
            result = 1
            for i in range(2, operand+1):
                result *= i
            return result
        else:
            raise ArithmeticError("Can't activate a factorial method on a fractional number.")
    else:
        raise ArithmeticError("Can't activate a factorial method on a negative number.")
