import string


def problem():
    print("Welcome to the calculator")

    num1 = float(input("What is the first number? "))
    operator = input("+,-,*,/ ")
    num2 = float(input("What is the second number? "))

    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            result = "undefined"
        else:
            result = num1 / num2
    else:
        print("Invalid operator")

    print(f"The result is {result}")

problem()