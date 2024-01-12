class Operator:

    def __init__(self, symbol: str, priority: int, position: int, unary: bool, method) -> None:
        """
        Create an operator object
        :param symbol: The symbol used to represent the operator.
        :param priority: An indicator to the operator's priority relative to the other operators
        (higher number indicates higher priority).
        :param position: The position in which the operator should be used(relative to the operands).
        -1 - left
        0 - in between
        1 - right
        :param unary: A flag for stating if the operator is unary.
        :param method: a reference to the method related to the operator
        """
        self.__symbol = symbol
        self.__priority = priority
        self.__position = position
        self.__unary = unary
        self.__method = method

    def getSymbol(self) -> str:
        """
        Get the operator's symbol
        :return: The operator's symbol
        """
        return self.__symbol

    def getPriority(self) -> int:
        """
        Get the operator's priority
        :return: The operator's priority
        """
        return self.__priority

    def getPosition(self) -> int:
        """
        Get the operator's position
        :return: The operator's position
        """
        return self.__position

    def isUnary(self) -> bool:
        """
        Check the operator's unary flag
        :return: True if unary and False otherwise
        """
        return self.__unary

    def getMethod(self):
        """
        Get the method related to the operator.
        :return: The operator's method reference
        """
        return self.__method
