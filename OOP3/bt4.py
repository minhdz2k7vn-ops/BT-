# ═══════════════════════════════════════════
#  LỚP 1: CON CHÓ
# ═══════════════════════════════════════════
class ConCho:
    def __init__(self, ten, mauSac, giong, camXuc="vui"):
        self.Ten = ten
        self.MauSac = mauSac
        self.Giong = giong
        self.CamXuc = camXuc

    def Sua(self):
        print(f"{self.Ten}: Gâu gâu! 🐕")

    def VayDuoi(self):
        print(f"{self.Ten} vẫy đuôi vì {self.CamXuc}!")

    def An(self, thucAn):
        print(f"{self.Ten} đang ăn {thucAn}. Ngon!")

    def Chay(self, tocDo):
        print(f"{self.Ten} chạy {tocDo} km/h!")


# ═══════════════════════════════════════════
#  LỚP 2: Ô TÔ
# ═══════════════════════════════════════════
class OTo:
    def __init__(self, hang, kichThuoc, mau, gia):
        self.Hang = hang
        self.KichThuoc = kichThuoc
        self.Mau = mau
        self.Gia = gia
        self.TocDo = 0

    def TangToc(self, them):
        self.TocDo += them
        print(f"Tăng tốc! Tốc độ hiện tại: {self.TocDo} km/h")

    def GiamToc(self, bot):
        self.TocDo = max(0, self.TocDo - bot)
        print(f"Giảm tốc! Tốc độ: {self.TocDo} km/h")

    def Dam(self):
        print(f"💥 Xe {self.Hang} bị đâm! Dừng khẩn cấp.")
        self.TocDo = 0


# ═══════════════════════════════════════════
#  LỚP 3: TÀI KHOẢN NGÂN HÀNG
# ═══════════════════════════════════════════
class TaiKhoan:
    def __init__(self, tenTK, soTK, nganHang, soDu=0):
        self.TenTK = tenTK
        self.SoTK = soTK
        self.NganHang = nganHang
        self._soDu = soDu

    def Gui(self, soTien):
        self._soDu += soTien
        print(f"✅ Gửi {soTien:,} VNĐ. Số dư: {self._soDu:,}")

    def Rut(self, soTien):
        if soTien > self._soDu:
            print("❌ Số dư không đủ!")
        else:
            self._soDu -= soTien
            print(f"✅ Rút {soTien:,} VNĐ. Còn: {self._soDu:,}")

    def KiemTraSoDu(self):
        print(f"💳 [{self.TenTK}] Số dư: {self._soDu:,} VNĐ")


# Main
if __name__ == "__main__":
    cho = ConCho("Milo", "vàng", "Golden Retriever")
    cho.Sua()
    cho.An("xương")

    xe = OTo("Toyota", "sedan", "trắng", 800_000_000)
    xe.TangToc(60)
    xe.TangToc(40)
    xe.GiamToc(30)

    tk = TaiKhoan("Nguyễn Văn A", "123456789", "Vietcombank", 5_000_000)
    tk.Gui(2_000_000)
    tk.Rut(3_000_000)
    tk.KiemTraSoDu()