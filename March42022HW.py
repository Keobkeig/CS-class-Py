magic_number = 4
while True:
    guess_number = int(input("Enter a guess: "))
    if guess_number > magic_number:
        print("Too high!")
    elif guess_number < magic_number:
        print("Too low!")
    elif guess_number == magic_number:
        print("Correct")
        break

