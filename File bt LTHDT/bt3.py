class SieuNhan:
    def __init__(self, ten, vuKhi, mauSac, sucManh):
        self.Ten = ten
        self.VuKhi = vuKhi
        self.MauSac = mauSac
        self.SucManh = sucManh

    def __str__(self):
        return f"  ✦ {self.Ten:<12} | Vũ khí: {self.VuKhi:<8} | Màu: {self.MauSac:<8} | Sức mạnh: {self.SucManh}"

# Main
if __name__ == "__main__":
    danhSach = []

    print("=== NHẬP DANH SÁCH SIÊU NHÂN ===")
    print("(Nhấn Enter để kết thúc)\n")

    while True:
        ten = input("Tên siêu nhân: ")
        if ten == "":
            break

        vuKhi = input("Vũ khí: ")
        mauSac = input("Màu sắc: ")
        sucManh = int(input("Sức mạnh (1-100): "))

        danhSach.append(SieuNhan(ten, vuKhi, mauSac, sucManh))
        print(f"  → Đã thêm {ten}!\n")

    print(f"\n=== DANH SÁCH {len(danhSach)} SIÊU NHÂN ===")
    i = 1
    for sn in danhSach:
        print(f"{i}.{sn}")
        i += 1