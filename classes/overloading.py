import math
class Point():

    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def __str__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    
    def __gt__(self, p):
        return self.distance() > p.distance()
    
    def __lt__(self, p):
        return self.distance() < p.distance()
    
    def __eq__(self, p):
        return self.x == p.x and self.y == p.y
    
    def __le__(self, p):
        return self.distance() <= p.distance()
    
    def __ge__(self, p):
        return self.distance() >= p.distance()
    
    def move(self, x, y):
        self.x += x
        self.y += y

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    
p1 = Point(3, 4)
p2 = Point(4, 6)

p_sum = p1 + p2

print(p_sum)
print(round(p_sum.distance(), 2))

print(p1 > p2)
 