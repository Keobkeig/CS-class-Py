def remove(word, remove):
    while True:
        if word.find(remove) == -1:
            return word
            break
        else: 
            word = word[:word.find(remove)] + word[word.find(remove) + len(remove):]
print(remove("bananas" , "na"))