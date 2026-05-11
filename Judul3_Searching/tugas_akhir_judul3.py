def sequential_search(data, n, target):
    i = 0
    posisi = []

    while i < n:
        if data[i].lower() == target.lower():
            posisi.append(i)
        i += 1

    return posisi


def tampilkan_data(data):
    print("\nDaftar File Dalam Folder:")
    for i in range(len(data)):
        print(f"{i + 1}. {data[i]}")


def tambah_file(data):
    nama = input("Masukkan nama file baru: ")
    data.append(nama)
    print("File berhasil ditambahkan!")


def hapus_file(data):
    nama = input("Masukkan nama file yang ingin dihapus: ")

    if nama in data:
        data.remove(nama)
        print("File berhasil dihapus!")
    else:
        print("File tidak ditemukan!")


def main():
    data = [
        "Tugas1.docx",
        "Tugas2.docx",
        "Laporan.pdf",
        "Data.xlsx",
        "Foto1.png",
        "Foto2.png",
        "Video.mp4",
        "MateriAI.pptx",
        "Musik.mp3",
        "CV.pdf",
        "Proposal.docx",
        "DataMahasiswa.xlsx",
        "TugasPython.py",
        "Catatan.txt",
        "JadwalKuliah.pdf"
    ]

    while True:
        print("\n===== MENU =====")
        print("1. Tampilkan File")
        print("2. Cari File")
        print("3. Tambah File")
        print("4. Hapus File")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            tampilkan_data(data)

        elif pilihan == "2":
            target = input("Masukkan nama file yang dicari: ")

            hasil = sequential_search(data, len(data), target)

            if len(hasil) > 0:
                print(f"\nFile '{target}' ditemukan!")

                for pos in hasil:
                    print(f"- Ditemukan pada urutan ke-{pos + 1}")

                print(f"Total ditemukan: {len(hasil)} file")

            else:
                print(f"\nFile '{target}' tidak ditemukan!")

        elif pilihan == "3":
            tambah_file(data)

        elif pilihan == "4":
            hapus_file(data)

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()