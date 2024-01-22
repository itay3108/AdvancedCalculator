from inputHandeling import validateInput, evalExpression
from operators.OpInCalculator import opDictionary


def calculate(expressionStr: str):
    """
    preforming all that is necessary for calculation and calculating
    :param expressionStr: The expression to calculate
    :return: The result of the calculation
    """
    expression = validateInput.validate_input(expressionStr)
    expression = validateInput.convertMinusesInExp(expression)
    return evalExpression.evalExpression(expression)


def Calculator():
    """
    The main function of the calculator called from main.
    :return: Presents the user with the menu of the calculator and acts accordingly.
    """
    programEnded = False
    print("Hello, welcome to my advanced calculator here are the actions you can make:")
    print("_____________________________________________\n"
          "c to calculate an expression\n"
          "h for help - list of available operators\n"
          "q for quiting - exiting the calculator\n")
    menuInput = input("please enter the action wanted: ")
    while not programEnded:
        if menuInput == 'c':
            try:
                string = input("\nplease enter an expression to calculate: ")
                print(calculate(string), "\n")
            except EOFError:
                print("The program was ended by the user.")
                programEnded = True
            except (SyntaxError, ArithmeticError) as e:
                print(e)
        elif menuInput == 'h':
            for op in opDictionary:
                if op != '?':  # not printing the unary minus
                    print(f"{op} - {opDictionary[op].getDescription()}")
            menuInput = input("please enter the action wanted: ")
        elif menuInput == 'q':
            print("The program was ended by the user.")
            programEnded = True
        else:
            print("please enter a valid option")
            menuInput = input("please enter the action wanted: ")
