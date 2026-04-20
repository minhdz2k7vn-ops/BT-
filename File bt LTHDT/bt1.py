import math

class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def HienThi(self):
        print(f"Điểm ({self.X}, {self.Y})")

    def DoiXungQuaO(self):
        return Point(-self.X, -self.Y)

    def KhoangCachDenO(self):
        return math.sqrt(self.X * self.X + self.Y * self.Y)

    def KhoangCachDen(self, other):
        return math.sqrt((self.X - other.X) ** 2 + (self.Y - other.Y) ** 2)

    def __str__(self):
        return f"({self.X}, {self.Y})"

# Main
if __name__ == "__main__":
    # Điểm A(3, 4)
    A = Point(3, 4)
    print("Điểm A: ", end="")
    A.HienThi()

    # Nhập điểm B từ bàn phím
    xb = int(input("Nhập x của B: "))
    yb = int(input("Nhập y của B: "))
    B = Point(xb, yb)
    print("Điểm B: ", end="")
    B.HienThi()

    # Điểm C đối xứng với B qua O
    C = B.DoiXungQuaO()
    print("Điểm C (đối xứng B qua O): ", end="")
    C.HienThi()

    # Khoảng cách
    print(f"Khoảng cách B đến O: {B.KhoangCachDenO():.2f}")
    print(f"Khoảng cách A đến B: {A.KhoangCachDen(B):.2f}")