# sum and difference of two numbers
# choice of user


# addition
def add(num1, num2):
    return f"The sum of {num1} and {num2} is {num1 + num2}"


# subtraction
def subtract(num1, num2):
    return f"The difference of {num1} and {num2} is {num1 - num2}"


# product
def multiply(num1, num2):
    return f"The product of {num1} and {num2} is {num1 * num2}"


# quotient
def divide(num1, num2):
    return f"The quotient of {num1} and {num2} is {num1 // num2}"


# operation
def operation(choice, num1, num2):
    match choice:
        case 1:
            print(add(num1, num2))
        case 2:
            print(subtract(num1, num2))
        case 3:
            print(multiply(num1, num2))
        case 4:
            print(divide(num1, num2))
        case _:
            print("Enter the choice between 1 and 4")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print()
print("Which operation do you want to perform?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Choice: "))
answer = operation(choice, num1, num2)