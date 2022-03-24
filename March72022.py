# cw1
for i in range(1, 7):
    for j in range (1, 7):
        print(str(i) + "," + str(j) )
# cw2 
def rainy():
    if weatherInput == "rainy":
        print("On a rainy day, galoshes are appropriate footwear.")
def snowy():
    if weatherInput == "snowy":
        print("On a snowy day, boots are appropriate footwear.")
def sunny():
        print("On a sunny day, boots are appropriate footwear.")
while True:
    weatherInput = int("What is the weather? ") 
    if weatherInput == "rainy":
        rainy()
    elif weatherInput == "snowy":
        snowy()
    elif weatherInput == "sunny":
        sunny()
    else: 
        print("Sorry, that's an invalid answer")
        break
