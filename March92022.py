num1 = 10 #global namespace variable
def adder(): 
    num2 = int(input("What is your second number: ")) #local namespace
    sum = num2 + num1 #local namespace
    print(sum) 
adder()