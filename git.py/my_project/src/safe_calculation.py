try:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        result = number1 + number2

    elif operator == "-":
        result = number1 - number2

    elif operator == "*":
        result = number1 * number2

    elif operator == "/":
        result = number1 / number2

    else:
        raise ValueError("Invalid operator")

    print("Result:", result)

except ValueError as e:
    print("Error:", e)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")