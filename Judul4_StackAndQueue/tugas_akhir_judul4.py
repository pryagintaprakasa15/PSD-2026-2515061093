class ParkirStack:
    def __init__(self, max_size=5):
        self.MAX = max_size
        self.mobil = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def mobil_masuk(self, plat):
        if self.is_full():
            print("Parkiran penuh!")
            return

        self.top_idx += 1
        self.mobil[self.top_idx] = plat
        print(f"Mobil {plat} masuk parkiran")

    def mobil_keluar(self):
        if self.is_empty():
            print("Parkiran kosong!")
            return

        print(f"Mobil {self.mobil[self.top_idx]} keluar parkiran")
        self.top_idx -= 1

    def mobil_terakhir(self):
        if self.is_empty():
            print("Parkiran kosong!")
            return

        print(f"Mobil terakhir: {self.mobil[self.top_idx]}")

    def tampilkan_parkiran(self):
        if self.is_empty():
            print("Parkiran kosong!")
            return

        print("Isi parkiran (depan keluar ke belakang):")
        for i in range(self.top_idx, -1, -1):
            print(self.mobil[i])


def main():
    parkir = ParkirStack()

    pilih = 0

    while pilih != 5:
        print("\n=== SISTEM PARKIR STACK ===")
        print("1. Mobil Masuk")
        print("2. Mobil Keluar")
        print("3. Lihat Mobil Terakhir")
        print("4. Tampilkan Parkiran")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka!")
            continue

        if pilih == 1:
            plat = input("Masukkan plat mobil: ")
            parkir.mobil_masuk(plat)

        elif pilih == 2:
            parkir.mobil_keluar()

        elif pilih == 3:
            parkir.mobil_terakhir()

        elif pilih == 4:
            parkir.tampilkan_parkiran()

        elif pilih == 5:
            print("Program selesai")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()