# Simple Calculator

def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: division by zero"


# Main code
while True:
    # Input operation
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter the operation number (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator.")
        break

    # Input numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform operation
    if choice == '1':
        print(num1, "+", num2, "=", addition(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtraction(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiplication(num1, num2))
    elif choice == '4':
        division_result = division(num1, num2)
        print(num1, "/", num2, "=", division_result)
    else:
        print("Invalid input. Please try again.")
