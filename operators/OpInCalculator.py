from operators import Operator, operatorFunctions

opDictionary = {
    '+': Operator.Operator('+', 1, 0, False, "Addition", operatorFunctions.add),
    '-': Operator.Operator('-', 1, 0, False, "Subtraction", operatorFunctions.sub),
    '*': Operator.Operator('*', 2, 0, False, "Multiplication", operatorFunctions.mul),
    '/': Operator.Operator('/', 2, 0, False, "Division", operatorFunctions.div),
    '?': Operator.Operator('?', 2.5, -1, True, "Unary Minus", operatorFunctions.neg),
    '^': Operator.Operator('^', 3, 0, False, "Power", operatorFunctions.power),
    '%': Operator.Operator('%', 4, 0, False, "Modulo", operatorFunctions.modulo),
    '@': Operator.Operator('@', 5, 0, False, "Find Average", operatorFunctions.avg),
    '$': Operator.Operator('$', 5, 0, False, "Find Maximum", operatorFunctions.maximum),
    '&': Operator.Operator('&', 5, 0, False, "Find Minimum", operatorFunctions.minimum),
    '~': Operator.Operator('~', 6, -1, True, "Negate", operatorFunctions.neg),
    '!': Operator.Operator('!', 6, 1, True, "Factorial", operatorFunctions.factorial),
    '#': Operator.Operator('#', 6, 1, True, "Digit Addition", operatorFunctions.digitAddition)
}
