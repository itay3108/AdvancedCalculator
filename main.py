from inputHandeling import validateInput


if __name__ == '__main__':
    try:
        string = input()
        expression = validateInput.convertMinusesInExp(validateInput.validate_input(string))
        print(expression)
    except SyntaxError as e:
        print(e)
