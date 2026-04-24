while True:
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2  = float(input("Enter second number: "))

    if op == "+":
        print("Result:", num1 + num2)

    elif op == "-":
        print("Result:", num1 - num2)

    elif op == "*":
        print("Result:", num1 * num2)

    elif op == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero!")

    else:
        print("Invalid operator!")

    choice = input("Do you want to continue? (yes/no): ").lower()
    if choice != "yes":
        print("Calculator closed.")
        break


       #OUTPUT

"""Enter first number: 12
Enter operator (+, -, *, /): +
Enter second number: 3
Result: 15.0
Do you want to continue? (yes/no): no
Calculator closed."""