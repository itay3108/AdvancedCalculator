from inputHandeling import validateInput


if __name__ == '__main__':
    try:
        string = "2+--3!"

        print(validateInput.validate_input(string))
    except SyntaxError and ArithmeticError as e:
        print(e)
