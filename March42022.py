studentAge = int(input("What is your age?: "))
if studentAge >= 13:
    print("welcom")
else:
    print("no")
if studentAge >= 16:
    guestBool = input("Do you have guest?: ")
    if guestBool >= "Yes":
        guestAge = int(input("Age: "))
    if guestAge >= 13:
        print("hi guest")
    else: 
        print("no guest")

    