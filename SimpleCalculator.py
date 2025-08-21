def calculator():
    print("Calculator Programme")
    num1 = float(input("Enter First Name"))
    operator = input("Enter the operator(+,-,*,/):")
    num2 = float(input("Enter Second Name"))

    if operator == "+":
        print("Result:", num1 + num2)
    elif operator == "-":
        print("Result:", num1 - num2)
    elif operator == "*":
        print("Result:", num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: cannot divide by zero")
    else:
        print("Invalid Operator")


calculator()
