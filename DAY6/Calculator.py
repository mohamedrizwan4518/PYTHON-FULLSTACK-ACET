def calc():
    try:
        a = float(input("Enter first number: "))
        op = input("Enter operator (+ - * /): ")
        b = float(input("Enter second number: "))

        if op == "+":
            print("Result:", a + b)

        elif op == "-":
            print("Result:", a - b)

        elif op == "*":
            print("Result:", a * b)

        elif op == "/":
            print("Result:", a / b)

        else:
            print("Invalid operator")

    except ZeroDivisionError:
        print("Cannot divide by zero!")
        calc()

    except ValueError:
        print("Enter valid input!")
        calc()

calc()
