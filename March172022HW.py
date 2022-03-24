import math

def distance(coordOne : tuple, coordTwo : tuple):
    xDiffResult = pow(coordOne[0] - coordTwo[0], 2)
    yDiffResult = pow(coordOne[1] - coordTwo[1], 2)
    return math.sqrt(xDiffResult + yDiffResult)
    
print(distance((3,2) , (0,2)))