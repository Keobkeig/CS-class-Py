'''
This is a program that asks the user to enter their full name and then prints it out
'''
first_name = input("Enter your first name: ")
#Asks the user to input their first name and then stores it into first_name 
middle_name = input("Enter your middle name: ")
#Asks the user to input their middle name and then stores it into middle_name
last_name = input("Enter your last name: ")
#Asks the user to input their last name and then stores it into last_name

full_name = first_name + " " + middle_name + " " + last_name
#Adds the inputted strings together to create a new variable, full_name
print(full_name)
#Whatever is inside full_name is printed out
