
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def move(self, dx, dy):
        self.a.x += dx
        self.b.x += dx
        self.c.x += dx
        self.d.x += dx

        self.a.y += dy
        self.b.y += dy
        self.c.y += dy
        self.d.y += dy

    def area(self):
        a = abs(self.a.x - self.b.x)
        b = abs(self.b.x - self.c.x)

        return a*b
        


p = Point(2, 3)
print(p.x, p.y) 

r = Rectangle(
    Point(1, 2),
    Point(5, 2),
    Point(5, 6),
    Point(1, 6)
)
r.move(2, -1)
print(r.a.x, r.b.y)
print(r.d.x, r.d.y)