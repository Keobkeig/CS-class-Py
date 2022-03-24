def count_occurences(word, letter):
    count = 0
    for amount in word:
        if letter in "word":
            count += 1
    return count
print(count_occurences("banana", "a"))