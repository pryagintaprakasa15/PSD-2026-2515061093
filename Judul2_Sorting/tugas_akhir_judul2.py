#PROGRAM MENGURUTKAN KODE BUKU DIPERPUSTAKAAN
def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def selection_sort(arr, n):
    for i in range(n - 1):
        pos = i
        for j in range(i + 1, n):
            if arr[j] < arr[pos]:
                pos = j
        if pos != i:
            tukar(arr, i, pos)

def main():
    try:
        n = int(input("Masukkan jumlah buku yang ingin diurutkan: "))
    except ValueError:
        print("Input tidak valid!")
        return

    arr = []
    print("Masukkan kode buku yang ingin diurutkan:")
    for i in range(n):
        while True:
            kode = input()
            if kode.strip() == "":
                print("Input tidak boleh kosong!")
            else:
                arr.append(kode)
                break

    print(f"Data buku sebelum diurutkan: {arr}")
    selection_sort(arr, n)
    print("Data buku setelah diurutkan:", arr)


    while True:
        print("\nPilih aksi:")
        print("1. Tambah data buku")
        print("2. Hapus data buku")
        print("3. Selesai mengurutkan buku.")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            kode = input("Masukkan kode buku baru: ")
            arr.append(kode)
            selection_sort(arr, len(arr))
            print("Data setelah ditambah & diurutkan:", arr)

        elif pilihan == "2":
            kode = input("Masukkan kode buku yang ingin dihapus: ")
            if kode in arr:
                arr.remove(kode)
                selection_sort(arr, len(arr))
                print("Data setelah dihapus & diurutkan:", arr)
            else:
                print("Data tidak ditemukan!")

        elif pilihan == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()