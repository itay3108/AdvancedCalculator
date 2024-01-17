from inputHandeling import validateInput, evalExpression
from operators.OpInCalculator import opDictionary


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
                expression = validateInput.convertMinusesInExp(validateInput.validate_input(string))
                print(evalExpression.evalExpression(expression), "\n")
            except EOFError:
                print("The program was ended by the user.")
                programEnded = True
            except (SyntaxError, ArithmeticError) as e:
                print(e)
        elif menuInput == 'h':
            for op in opDictionary:
                if op != '?':
                    print(f"{op} - {opDictionary[op].getDescription()}")
            menuInput = input("please enter the action wanted: ")
        elif menuInput == 'q':
            print("The program was ended by the user.")
            programEnded = True
        else:
            print("please enter a valid option")
            menuInput = input("please enter the action wanted: ")
