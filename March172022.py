# cw1
my_tuple = (0, 1, 2, "hi", 4, 5)
my_tuple = (my_tuple[:3] + (3,) + (my_tuple[4:]))
print(my_tuple)
# cw2
def citation(first, middle, last):
    return last + ", " + middle + " " + first 
print(citation("Martin", "Luther", "King, Jr."))