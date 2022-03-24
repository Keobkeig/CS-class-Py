my_list = [5, 2, -5, 10, 23, -21]
def max_int_in_list(items :list):
    maximum = list[0]
    for num in items:
        if num > maximum:
            maximum = num
    return "bigest_int is now " + str(maximum)
print(max_int_in_list(my_list))