# hw 1
def add_enthusiasm(word):
    return word.upper() + "!"
print(add_enthusiasm("hi"))
# hw 2
def name_contains(name, letter):
    if name.find(letter) > -1:
        return True
    else: 
        return False
print(name_contains("Richie", "c"))
print(name_contains("Jack", "u"))