class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def move(self, dx, dy):
        self.p1.x += dx
        self.p1.y += dy

        self.p2.x += dx
        self.p2.y += dy

        self.p3.x += dx
        self.p3.y += dy

        self.p4.x += dx
        self.p4.y += dy

    def contains_point(self, point):
        recx = [self.p1.x, self.p2.x, self.p3.x, self.p4.x]
        recy = [self.p1.y, self.p2.y, self.p3.y, self.p4.y]

        min_x = min(recx)
        min_y = min(recy)

        max_x = max(recx)
        max_y = max(recy)

        self.point = point

        if point.x <= max_x and point.y <= max_y and point.x >= min_x and point.y >= min_y:
            return True
        else:
            return False
        

    def scale(self, factor):
        points = [self.p1, self.p2, self.p3, self.p4]

        min_x = min(p.x for p in points)
        min_y = min(p.y for p in points)  

        for p in points:
            p.x = min_x + (p.x - min_x) * factor
            p.y = min_y + (p.y - min_y) * factor


r = Rectangle(
    Point(1, 2),
    Point(5, 2),
    Point(5, 6),
    Point(1, 6))

bod = Point(3, 40)

print (r.contains_point(bod))