num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
operation = input("Choose an operation (add, subtract, multiply): ")
def addition():
    sum = num1 + num2
    print(str(num1) + " + " + str(num2) + " = " + str(sum))
def subtraction():
    difference = num1 - num2
    print(str(num1) + " - " + str(num2) + " = " + str(difference))
def multiplication():
    product = num1 * num2
    print(str(num1) + " * " + str(num2) + " = " + str(product))
if operation == "add":
    addition()
elif operation == "subtract":
    subtraction()
elif operation == "multiply":
    multiplication()
else:
    print("That's an invalid operation!")