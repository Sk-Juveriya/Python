age=int(input("Enter age:"))
try:
    if age<18:
        raise ValueError("You must grow older")
    print("You can vote")
except ValueError as e:
    print("Error:", e)
finally:
    print("Code executed successfully")



try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except ValueError:
    print("Error: Please enter valid integers.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

else:
    print("Result =", result)

finally:
    print("Program execution completed.")