class Gerbong:
    def __init__(self, nama):
        self.nama = nama
        self.next = None


class KeretaApi:
    def __init__(self):
        self.kepala = None

    def tambah_gerbong(self, nama):
        baru = Gerbong(nama)
        if self.kepala is None:
            self.kepala = baru
            return
        
        sekarang = self.kepala
        while sekarang.next:
            sekarang = sekarang.next
        sekarang.next = baru

    def tambah_di_posisi(self, nama, posisi):
        baru = Gerbong(nama)

        if posisi == 0:
            baru.next = self.kepala
            self.kepala = baru
            return

        sekarang = self.kepala
        for i in range(posisi - 1):
            if sekarang is None:
                print("Posisi tidak valid")
                return
            sekarang = sekarang.next

        baru.next = sekarang.next
        sekarang.next = baru

    def hapus_gerbong(self, nama):
        sekarang = self.kepala

        if sekarang and sekarang.nama == nama:
            self.kepala = sekarang.next
            return

        prev = None
        while sekarang and sekarang.nama != nama:
            prev = sekarang
            sekarang = sekarang.next

        if sekarang is None:
            print("Gerbong tidak ditemukan")
            return

        prev.next = sekarang.next

    def ganti_lokomotif(self, nama_baru):
        if self.kepala is None:
            print("Kereta kosong")
            return
        
        self.kepala.nama = nama_baru

    def tampilkan(self):
        sekarang = self.kepala
        if sekarang is None:
            print("Kereta kosong")
            return

        while sekarang:
            print(f"[{sekarang.nama}]", end=" -> ")
            sekarang = sekarang.next
        print("None")


# ======================
# Program utama (menu)
# ======================
kereta = KeretaApi()

while True:
    print("\n=== MENU KERETA API ===")
    print("1. Tambah gerbong")
    print("2. Tambah gerbong di posisi tertentu")
    print("3. Hapus gerbong")
    print("4. Ganti lokomotif")
    print("5. Tampilkan kereta")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Masukkan nama gerbong: ")
        kereta.tambah_gerbong(nama)

    elif pilihan == "2":
        nama = input("Masukkan nama gerbong: ")
        posisi = int(input("Masukkan posisi (mulai dari 0): "))
        kereta.tambah_di_posisi(nama, posisi)

    elif pilihan == "3":
        nama = input("Masukkan nama gerbong yang ingin dihapus: ")
        kereta.hapus_gerbong(nama)

    elif pilihan == "4":
        nama = input("Masukkan nama lokomotif baru: ")
        kereta.ganti_lokomotif(nama)

    elif pilihan == "5":
        kereta.tampilkan()

    elif pilihan == "6":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")