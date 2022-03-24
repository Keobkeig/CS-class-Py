def cToF():
    celsius = float(input("What is the temp in C: "))
    return (celsius * 1.8) + 32
def fToC():
    fahrenheit = float(input("What is the temp in F: "))
    return (fahrenheit - 32) / 1.8
try:
    print("It is: " + str(cToF()) + " F")
    print("It is: " + str(fToC()) + " C")
except ValueError:
    print("That can't be converted into a float! ")
