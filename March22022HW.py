userAge = int(input("Age: "))
userCitizen = (input("US Citizenship: "))
userLOR = int(input("Years of Residency: "))
if userAge >= 35 and userCitizen == "Yes" and userLOR >= 14:
    print("Age:" + str(userAge))
    print("Born in the U.S.? (Yes/No): " + str(userCitizen))
    print("Years of Residency: " + str(userLOR))
    print("You are eligible to run for president! ")
else:
    print("Age:" + str(userAge))
    print("Born in the U.S.? (Yes/No): " + str(userCitizen))
    print("Years of Residency: " + str(userLOR))
    print("You are not eligible to run for president! ")
