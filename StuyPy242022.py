from cmath import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_distance(self, to_point):
        return sqrt((to_point.x - self.x)**2 + (to_point.y - self.y)**2)
class Triangle:
    def __init__(self, pointA, pointB, pointC):
        self.pointA = pointA
        self.pointB = pointB
        self.pointC = pointC
    def get_perimeter(self):
        return self.pointA.get_distance(self.pointB) + self.pointA.get_distance(self.pointC) + self.pointC.get_distance(self.pointB)
point1 = Point(0,0)
point2 = Point(3,0)
point3 = Point(0,4)
pointy = Triangle(point1, point2, point3)
print(pointy.get_perimeter())

