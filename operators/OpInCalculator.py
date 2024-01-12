
from operators import currentOPFunctions
from operators import Operator

opDictionary = {
    '+': Operator.Operator('+', 1, 0, False, currentOPFunctions.add),
    '-': Operator.Operator('-', 1, 0, False, currentOPFunctions.sub),
    '*': Operator.Operator('*', 2, 0, False, currentOPFunctions.mul),
    '/': Operator.Operator('/', 2, 0, False, currentOPFunctions.div),
    '^': Operator.Operator('^', 3, 0, False, currentOPFunctions.power),
    '%': Operator.Operator('%', 4, 0, False, currentOPFunctions.modulo),
    '@': Operator.Operator('@', 5, 0, False, currentOPFunctions.avg),
    '$': Operator.Operator('$', 5, 0, False, currentOPFunctions.maximum),
    '&': Operator.Operator('&', 5, 0, False, currentOPFunctions.minimum),
    '~': Operator.Operator('~', 6, -1, True, currentOPFunctions.neg),
    '!': Operator.Operator('!', 6, 1, True, currentOPFunctions.factorial),
    '#': Operator.Operator('#', 6, 1, True, currentOPFunctions.digitAddition)
}
