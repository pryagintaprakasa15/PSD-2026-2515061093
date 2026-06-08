class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE
        self.count = 0

    def hash_function(self, key):
        return key % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]

        while current:
            if current.key == key:
                current.value = value
                print("Data berhasil diperbarui.")
                return
            current = current.next

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.count += 1
        print("Data berhasil ditambahkan.")

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current
            current = current.next

        return None

    def remove_key(self, key):
        index = self.hash_function(key)

        current = self.table[index]
        prev = None

        while current:

            if current.key == key:

                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next

                self.count -= 1
                print("Data berhasil dihapus.")
                return

            prev = current
            current = current.next

        print("Data tidak ditemukan.")

    def display(self):

        print("\n========== ISI HASH TABLE ==========")

        for i in range(self.SIZE):

            print(f"Bucket {i} :", end=" ")

            current = self.table[i]

            while current:
                print(f"[{current.key}:{current.value}] -->", end=" ")
                current = current.next

            print("NULL")

    def total_data(self):
        print("\nJumlah data :", self.count)

    def load_factor(self):
        print("\nLoad Factor =", self.count / self.SIZE)

    def tampil_bucket(self, index):

        if index < 0 or index >= self.SIZE:
            print("Bucket tidak valid")
            return

        print(f"\nBucket {index}")

        current = self.table[index]

        while current:
            print(f"{current.key} : {current.value}")
            current = current.next

        if self.table[index] is None:
            print("Kosong")

    def clear(self):

        self.table = [None] * self.SIZE
        self.count = 0
        print("\nSemua data berhasil dihapus.")


def menu():

    hashmap = HashMapSeparateChaining()

    while True:

        print("\n===== KAMUS DIGITAL =====")
        print("1. Tambah Data")
        print("2. Cari Data")
        print("3. Hapus Data")
        print("4. Tampilkan Semua")
        print("5. Jumlah Data")
        print("6. Load Factor")
        print("7. Tampilkan Bucket")
        print("8. Hapus Semua Data")
        print("9. Keluar")

        pilih = int(input("Pilih menu : "))

        if pilih == 1:

            key = int(input("Masukkan ID Kata : "))
            arti = input("Masukkan Arti Kata : ")

            hashmap.insert(key, arti)

        elif pilih == 2:

            key = int(input("Masukkan ID yang dicari : "))

            hasil = hashmap.search(key)

            if hasil:
                print("Data ditemukan")
                print("ID :", hasil.key)
                print("Arti :", hasil.value)
            else:
                print("Data tidak ditemukan.")

        elif pilih == 3:

            key = int(input("Masukkan ID yang akan dihapus : "))
            hashmap.remove_key(key)

        elif pilih == 4:

            hashmap.display()

        elif pilih == 5:

            hashmap.total_data()

        elif pilih == 6:

            hashmap.load_factor()

        elif pilih == 7:

            bucket = int(input("Masukkan nomor bucket : "))
            hashmap.tampil_bucket(bucket)

        elif pilih == 8:

            hashmap.clear()

        elif pilih == 9:

            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    menu()