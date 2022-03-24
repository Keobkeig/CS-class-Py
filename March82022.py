# cw1
def calculate_area(side_length):
    if side_length <= 0: 
        calculate_area(10)
    else:
        area = side_length * side_length
        print("The area of a square with sides of length " + str(side_length) + " is " + str(area))

calculate_area(int(input("Enter side length: ")))