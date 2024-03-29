from operators.OpInCalculator import opDictionary


def tryNumConversion(num: str) -> bool:
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


def closeExp(dividedExp: list, index: int):
    """
    Closing an open expression duo to a '-' conversion
    :param dividedExp: The expression needed to be closed
    :param index: The position of the start of the expression
    :return: Update the expression accordingly
    """
    openedExp = 1
    j = index + 1
    placeToAddFound = False
    while not placeToAddFound and j < len(dividedExp) - 1:
        if dividedExp[j] == '(':
            openedExp += 1
        elif dividedExp[j] == ')':
            openedExp -= 1
            if openedExp == 0:
                placeToAddFound = True
        j += 1
    dividedExp[j-1:j] = [dividedExp[j-1], ')']


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
        if index < len(dividedExp)-1:
            after = dividedExp[index+1]
            if after != ')' and not (after in opDictionary and opDictionary[after].getPosition() != -1):
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
        before = dividedExp[index - 1]
        after = dividedExp[index + 1]
        if after != '(' and not tryNumConversion(after) and after != '-':
            notValid = True
        if not (before in opDictionary and not opDictionary[before].isUnary()) and before != '(':
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
                if dividedExp[index + 1] in opDictionary and dividedExp[index + 1] != '-':
                    raise SyntaxError("Syntax Error: '-' operator can't be followed by an operator excluding '-'")
        elif index == len(dividedExp) - 1:
            notValid = True
        else:
            after = dividedExp[index + 1]
            before = dividedExp[index - 1]
            if after != '-' and after != '(' and not tryNumConversion(after):
                if after in opDictionary and opDictionary[after].getPosition() == -1:
                    if before in opDictionary and opDictionary[before].getPosition() != 1:
                        raise SyntaxError("Syntax Error: '-' cannot be preceded by a non-post unary operator and "
                                          "followed by a non-post unary operator except '-' operator")
                else:
                    raise SyntaxError("Syntax Error: '-' operator can't be followed by a non-pre unary operator")

    elif 0 < index < len(dividedExp) - 1:
        before = dividedExp[index - 1]
        after = dividedExp[index + 1]
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


def convertMinusesInExp(dividedExp: list) -> list:
    """
    Converting all the unary minuses to 0 - the operand/expression and maintaining the priority of the expression.
    :param dividedExp: The expression that may need the conversion.
    :return: The divided expression changed if needed.
    """
    nonBinaryMinus = False
    startingStreak = 0
    i = 0
    while i < len(dividedExp):
        if dividedExp[i] == '-':
            if len(dividedExp)-1 > i > 0 > startingStreak:
                before = dividedExp[i - 1]
                if before in opDictionary and opDictionary[before].getPosition() != 1:
                    dividedExp[i:i + 1] = ['(', 0, '-']
                    nonBinaryMinus = True
                    i += 2

                elif before == '(':
                    dividedExp[i:i + 1] = ['?']
                    i += 1

                if nonBinaryMinus:
                    parenthesisAdded = False
                    j = i+1
                    while not parenthesisAdded and j < len(dividedExp):
                        if dividedExp[j] == '(':
                            closeExp(dividedExp, j)
                            parenthesisAdded = True
                            j += 1
                        elif tryNumConversion(dividedExp[j]):
                            dividedExp[j:j+1] = [dividedExp[j], ')']
                            parenthesisAdded = True
                        j += 1
                    nonBinaryMinus = False
            else:
                startingStreak += 1
        else:
            if dividedExp[startingStreak-1] == '-':
                if startingStreak % 2 == 0:
                    dividedExp[i-startingStreak:i] = []
                    i -= startingStreak
                elif startingStreak != -1 and startingStreak % 2 == 1:
                    dividedExp[i-startingStreak:i] = ['?']
                    startingStreak -= startingStreak-1
            startingStreak = -1
        i += 1
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

    i = 0
    if len(dividedExp) > 0:
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
                if dividedExp[i] in opDictionary and dividedExp[i] != '?':
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
                    if i > 0 and tryNumConversion(dividedExp[i-1]):
                        raise SyntaxError("Syntax error: Illegal operand placement before an opening parenthesis.")
                    openedExpression += 1
                elif dividedExp[i] == ')':
                    if openedExpression <= 0:
                        raise SyntaxError("Syntax error: Unmatched closing parenthesis.")
                    elif i < len(dividedExp)-1 and tryNumConversion(dividedExp[i+1]):
                        raise SyntaxError("Syntax error: There shouldn't be a number after a closing parenthesis.")
                    else:
                        if (dividedExp[i - 1] == '(' or
                                (dividedExp[i - 1] in opDictionary and opDictionary[dividedExp[i - 1]].getPosition() <= 0)):
                            raise SyntaxError("Syntax error: There is no expression between the parentheses.")
                        else:
                            openedExpression -= 1
                else:
                    raise SyntaxError(f"Syntax error: Unknown operator '{dividedExp[i]}'.")
                i += 1

        if openedExpression > 0:
            raise SyntaxError("Syntax error: Unmatched opening parenthesis.")

        return dividedExp
    else:
        raise SyntaxError("Syntax error: Empty expression.")
