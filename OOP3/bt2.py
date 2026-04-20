class SieuNhan:
    def __init__(self, ten, vuKhi, mauSac):
        self.Ten = ten
        self.VuKhi = vuKhi
        self.MauSac = mauSac

    def __str__(self):
        return f"Siêu nhân {self.Ten:<10} | Vũ khí: {self.VuKhi:<8} | Màu: {self.MauSac}"

# Main
if __name__ == "__main__":
    sieuNhanA = SieuNhan("A", "kiếm", "đỏ")
    sieuNhanB = SieuNhan("B", "khiên", "xanh")

    print(sieuNhanA)
    print(sieuNhanB)