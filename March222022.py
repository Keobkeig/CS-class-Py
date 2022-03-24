# cw1
from re import S


def amtOfNames():
    number = int(input("Number of names: "))
    name = []
    for i in range(number):
        addName = input("Name: ")
        name.append(addName)
    print("First name: " + str(name[0]))
    print("Middle name: " + str(name[1:-1]))
    print("Last name: " + str(name[-1]))
amtOfNames()
# cw2
def bigList():
    numberList = []
    for i in range(5):
        ask = int(input("Number: "))
        added = numberList.append(ask)
        print(numberList)
    print(numberList[0] + numberList[1] + numberList[2] + numberList[3] + numberList[4])
bigList()
    