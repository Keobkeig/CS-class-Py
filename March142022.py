# cw 1
def sandwich(threeLString):
    return(threeLString[0] + threeLString[2])
print(sandwich("pbj"))
# cw 2
def replace_at_index(string, indexNumber):
    return (string[:indexNumber] + "-" + string[indexNumber + 1 :])
print(replace_at_index("Pizza", 2))
# cw 3
def replace_at_index2(string1, newIndexNumber, string2):
    return (string1[:newIndexNumber] + string2 + string1[newIndexNumber + 1:])
print(replace_at_index2("Pizza", 3, "p"))