# cw1
def contains_vowel(word):
    for vowel in "aeiou":
        if vowel in word:
            return True
    return False
print(contains_vowel("hello"))
    