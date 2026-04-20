import math

class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y


class Rectangle:
    def __init__(self, corner, w, h):
        self.Corner = corner  # góc dưới-trái
        self.Width = w
        self.Height = h


class Circle:
    def __init__(self, center, radius):
        self.Center = center
        self.Radius = radius


class GeometryHelper:
    @staticmethod
    def Distance(a, b):
        return math.sqrt((a.X - b.X) ** 2 + (a.Y - b.Y) ** 2)

    @staticmethod
    def PointInCircle(c, p):
        return GeometryHelper.Distance(c.Center, p) <= c.Radius

    @staticmethod
    def RectInCircle(c, r):
        corners = [
            Point(r.Corner.X, r.Corner.Y),
            Point(r.Corner.X + r.Width, r.Corner.Y),
            Point(r.Corner.X, r.Corner.Y + r.Height),
            Point(r.Corner.X + r.Width, r.Corner.Y + r.Height)
        ]
        for p in corners:
            if not GeometryHelper.PointInCircle(c, p):
                return False
        return True

    @staticmethod
    def RectCircleOverlap(c, r):
        corners = [
            Point(r.Corner.X, r.Corner.Y),
            Point(r.Corner.X + r.Width, r.Corner.Y),
            Point(r.Corner.X, r.Corner.Y + r.Height),
            Point(r.Corner.X + r.Width, r.Corner.Y + r.Height)
        ]
        for p in corners:
            if GeometryHelper.PointInCircle(c, p):
                return True
        return False


# Main
if __name__ == "__main__":
    circle = Circle(Point(150, 100), 75)

    p1 = Point(150, 100)  # tâm → trong
    p2 = Point(300, 300)  # xa   → ngoài
    print(f"p1 trong vòng tròn: {GeometryHelper.PointInCircle(circle, p1)}")
    print(f"p2 trong vòng tròn: {GeometryHelper.PointInCircle(circle, p2)}")

    rectSmall = Rectangle(Point(140, 90), 10, 10)
    rectLarge = Rectangle(Point(100, 50), 300, 200)
    print(f"rectSmall trong circle: {GeometryHelper.RectInCircle(circle, rectSmall)}")
    print(f"rectLarge overlap circle: {GeometryHelper.RectCircleOverlap(circle, rectLarge)}")