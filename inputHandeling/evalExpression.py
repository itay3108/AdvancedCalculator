from operators.OpInCalculator import opDictionary


def apply_operator(operator, operand1, operand2=None):
    """
    Applying a single operator from the expression.
    :param operator: The operator to aplay
    :param operand1: The first operand - must be a value
    :param operand2: The second operand - is a value in binary operator and None in unary operator
    :return:
    """
    if operand2 is None:  # Unary operator
        return opDictionary[operator].getMethod()(operand1)

    else:  # Binary operator
        return opDictionary[operator].getMethod()(operand1, operand2)


def findMaxPriority(expression: list) -> int:
    """
    Finding the index of the first operator with the highest priority.
    :param expression: The list to search operators at.
    :return: The index of the first operator with the highest priority.
    """
    i = 0
    maxIndex = -1
    while i < len(expression):
        if expression[i] in opDictionary:
            if maxIndex == -1:
                maxIndex = i
            elif opDictionary[expression[i]].getPriority() > opDictionary[expression[maxIndex]].getPriority():
                maxIndex = i
        i += 1
    return maxIndex


def evalExpression(expression: list):
    print(expression)
    """
    Calculating the given expression using the operators methods
    :param expression: The expression needed to be calculated
    :return: The result of the expression
    """
    stack_values = []
    stack_operators = []

    for token in expression:
        if token == '(':
            stack_operators.append(token)
        elif token == ')':
            while stack_operators and stack_operators[-1] != '(':
                operator = stack_operators.pop()
                operand2 = stack_values.pop()

                if opDictionary[operator].isUnary():
                    stack_values.append(apply_operator(operator, operand2))
                else:
                    operand1 = stack_values.pop()
                    stack_values.append(apply_operator(operator, operand1, operand2))

            stack_operators.pop()  # Pop the '('
        elif token in opDictionary:
            current_operator = opDictionary[token]

            while (
                    stack_operators
                    and stack_operators[-1] != '('
                    and opDictionary[stack_operators[-1]].getPriority() >= current_operator.getPriority()
            ):
                operator = stack_operators.pop()
                operand2 = stack_values.pop()

                if opDictionary[operator].isUnary():
                    stack_values.append(apply_operator(operator, operand2))
                else:
                    operand1 = stack_values.pop()
                    stack_values.append(apply_operator(operator, operand1, operand2))

            stack_operators.append(token)
        else:
            stack_values.append(token)

    while stack_operators:
        operator = stack_operators.pop()
        operand2 = stack_values.pop()

        if opDictionary[operator].isUnary():
            stack_values.append(apply_operator(operator, operand2))
        else:
            operand1 = stack_values.pop()
            stack_values.append(apply_operator(operator, operand1, operand2))

    return stack_values[0]
