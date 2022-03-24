# cw 1
def cToF(celsius):
    return (celsius * 1.8) + 32
def fToC(fahrenheit):
    return (fahrenheit - 32) / 1.8

print("It is: " + str(cToF(0)) + " F")
print("It is: " + str(cToF(100)) + " F")
print("It is: " + str(fToC(40)) + " C")
print("It is: " + str(fToC(80)) + " C")