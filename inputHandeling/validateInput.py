from operators.OpInCalculator import opDictionary


def isInt(num):
    """
    Checks if a num is an int.
    :param num: The num to check.
    :return: True if so and False otherwise.
    """
    return isinstance(num, int)


def tryNumConversion(num: str):
    """
    Tries converting the string to a number
    :param num: The possible number's string
    :return: True if the conversion was successful and False otherwise
    """
    try:
        float(num)
        return True
    except ValueError:
        return False


def isFloat(num):
    """
    Checks if a num is a float.
    :param num: The num to check.
    :return: True if so and False otherwise.
    """
    return isinstance(num, float)


def checkUnaryPostOp(dividedExp: list, index: int):
    """
    Checking the position of the post operand unary operators
    :param dividedExp: The expression to calculate (already divided into a list).
    :param index: The index of the operator needed to be checked.
    :return: commits the wanted check and raises a syntax error if not in the terms of use of this operator type.
    :raises SyntaxError: If the operator is before a closing parenthesis, a non-unary operator.
    """
    notValid = False
    if index != 0:
        if index < len(dividedExp) - 1:
            after = dividedExp[index-1]
            if after != ')' and not (after in opDictionary and not opDictionary[after].isUnary()):
                notValid = True
    else:
        notValid = True
    if notValid:
        raise SyntaxError(f"Syntax error: Post operand unary operator '{dividedExp[index]}' must be followed by an non "
                          f"unary operator or closing parenthesis.")


def checkUnaryPreOp(dividedExp: list, index: int):
    """
    Checking the position of the pre operand unary operators
    :param dividedExp: The expression to calculate (already divided into a list).
    :param index: The index of the operator needed to be checked.
    :return: commits the wanted check and raises a syntax error if not in the terms of use of this operator type.
    :raises SyntaxError: If the operator is not before an opening parenthesis, a number, or a '-' operator.
    """
    notValid = False
    if 0 < index < len(dividedExp) - 1:
        after = dividedExp[index + 1]
        before = dividedExp[index-1]
        if after != '(' and not tryNumConversion(after) and after != '-':
            notValid = True
        if not (before in opDictionary and not opDictionary[before].isUnary()):
            raise SyntaxError(f"Syntax error: Pre operand unary operator '{dividedExp[index]}' must be preceded by a "
                              f"non-unary operator.")
    elif index == 0:
        after = dividedExp[index + 1]
        if after != '(' and not tryNumConversion(after) and after != '-':
            notValid = True
    else:
        notValid = True
    if notValid:
        raise SyntaxError(f"Syntax error: Pre operand unary operator '{dividedExp[index]}' must be followed by a "
                          f"number, '-' operator or an opening parenthesis.")


def checkBinaryOp(dividedExp: list, index: int):
    """
    Checking the position of the binary operators (except '-' operator)
    :param dividedExp: The expression to calculate (already divided into a list).
    :param index: The index of the operator needed to be checked.
    :return: commits the wanted check and raises a syntax error if not in the terms of use of this operator type.
    :raises SyntaxError: If the operator is not surrounded by unary operands or a closing parenthesis before and
            an opening one after.
    """
    notValid = False
    if dividedExp[index] == '-':
        if index == 0:
            if len(dividedExp) - 1 > 0:
                if dividedExp[index + 1] in opDictionary and opDictionary[dividedExp[index + 1]] != '-':
                    raise SyntaxError("Syntax Error: '-' operator can't be followed by an operator excluding '-'")
        elif index == len(dividedExp) - 1:
            notValid = True
        else:
            after = dividedExp[index + 1]
            if after != '-' and after != '(' and not tryNumConversion(after) and not (
                    after in opDictionary and opDictionary[after].getPosition() == -1):
                raise SyntaxError("Syntax Error: '-' operator must be followed by a number or closing parenthesis or "
                                  "another '-' operator")
    elif 0 < index < len(dividedExp) - 1:
        before = dividedExp[index - 1]
        after = dividedExp[index + 1]
        print(before)
        print(after, "\n")
        if (after != '(' and not tryNumConversion(after) and after != '-' and not (
                after in opDictionary and opDictionary[after].getPosition() == -1)):
            notValid = True
        if before != ')' and not tryNumConversion(before) and (
                before in opDictionary and opDictionary[before].getPosition() != 1):
            notValid = True
    else:
        notValid = True
    if notValid:
        raise SyntaxError(f"Syntax Error: Binary operator '{dividedExp[index]}' must be surrounded by operands or "
                          f"unary operands or a closing parenthesis before and an opening one after.")


def convertMinusesInExp(dividedExp: list):
    """
    Converting all the unary minuses to 0 - the operand/expression and maintaining the priority of the expression.
    :param dividedExp: The expression that may need the conversion.
    :return: The divided expression changed if needed.
    """
    i = 0
    while i < len(dividedExp):
        if dividedExp[i] == '-':
            if 0 < i < len(dividedExp) - 1:
                after = dividedExp[i + 1]
                if after == '(':
                    openedExp = 1
                    j = i + 1
                    while openedExp > 0:
                        if dividedExp[j] == '(':
                            openedExp += 1
                        elif dividedExp[j] == ')':
                            openedExp -= 1
                        j += 1
                    dividedExp[j:j + 1] = [dividedExp[j], ')']
                else:
                    dividedExp[i + 1:i + 2] = [dividedExp[i + 1], ')']
                before = dividedExp[i - 1]
                if before in opDictionary and opDictionary[before].getPosition() != 1:
                    dividedExp[i:i + 1] = ['(', 0, '-']
                    i += 3
                else:
                    raise SyntaxError("Syntax error: The operator '-' has no operand after it.")
            else:
                dividedExp[i:i + 1] = [0, '-']
    return dividedExp


def validate_input(expression: str) -> list:
    """
    Validating the input from the user (called before the evaluation of the expression)
    :param expression: The expression to validate
    :return: List representing the validated expression
    :raises SyntaxError: If the expression is not valid
    """
    openedExpression = 0
    expression = (expression.replace(" ", "")
                  .replace("\t", "")
                  .replace("\n", ""))
    dividedExp = list(expression)
    print(dividedExp)

    i = 0
    while i < len(dividedExp):
        operand = ""
        while i < len(dividedExp) and (dividedExp[i].isdigit() or (dividedExp[i] == '.')):
            operand += dividedExp[i]
            i += 1

        if operand:
            try:
                dividedExp[i - len(operand):i] = [int(operand)]
            except ValueError:
                try:
                    dividedExp[i - len(operand):i] = [float(operand)]
                except ValueError:
                    raise SyntaxError(f"Syntax error: Illegal operand: '{operand}'")
            i = i - len(operand) + 1

        else:
            if dividedExp[i] in opDictionary:
                op = opDictionary[dividedExp[i]]
                if (op.getPosition() == 1 and i == 0) or (op.getPosition() == -1 and i == len(dividedExp) - 1):
                    raise SyntaxError(f"Syntax error: Operator '{dividedExp[i]}' not in a legal position.")
                if op.getPosition() == 1:
                    checkUnaryPostOp(dividedExp, i)
                elif op.getPosition() == -1:
                    checkUnaryPreOp(dividedExp, i)
                else:
                    checkBinaryOp(dividedExp, i)

            elif dividedExp[i] == '(':
                openedExpression += 1
            elif dividedExp[i] == ')':
                if openedExpression <= 0:
                    raise SyntaxError("Syntax error: Unmatched closing parenthesis.")
                else:
                    if (dividedExp[i - 1] == '(' or
                            (dividedExp[i - 1] in opDictionary and opDictionary[dividedExp[i - 1]].getPosition() <= 0)):
                        raise SyntaxError("Syntax error: there is no expression between the parentheses.")
                    else:
                        openedExpression -= 1
            else:
                raise SyntaxError(f"Syntax error: Unknown operator '{dividedExp[i]}'.")
            i += 1

    if openedExpression > 0:
        raise SyntaxError("Syntax error: Unmatched opening parenthesis.")

    return convertMinusesInExp(dividedExp)
