class Node:
    def __init__(self, lokasi, jarak):
        self.lokasi = lokasi
        self.jarak = jarak
        self.left = None
        self.right = None


class BSTNavigasiGPS:
    def __init__(self):
        self.root = None

    # Menambahkan lokasi
    def insert_node(self, root, lokasi, jarak):
        if root is None:
            return Node(lokasi, jarak)

        if jarak < root.jarak:
            root.left = self.insert_node(root.left, lokasi, jarak)

        elif jarak > root.jarak:
            root.right = self.insert_node(root.right, lokasi, jarak)

        return root

    def insert(self, lokasi, jarak):
        self.root = self.insert_node(self.root, lokasi, jarak)

    # Menampilkan semua lokasi (urut jarak)
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)

            print(f"{root.lokasi} - {root.jarak} KM")

            self.inorder(root.right)

    # Cari lokasi berdasarkan jarak
    def search(self, root, jarak):
        if root is None:
            return None

        if jarak == root.jarak:
            return root

        if jarak < root.jarak:
            return self.search(root.left, jarak)

        return self.search(root.right, jarak)

    # Cari lokasi terdekat
    def find_min(self, root):
        current = root

        while current is not None and current.left is not None:
            current = current.left

        return current

    # Cari lokasi terjauh
    def find_max(self, root):
        current = root

        while current is not None and current.right is not None:
            current = current.right

        return current

    # Menghapus lokasi
    def delete_node(self, root, jarak):
        if root is None:
            return None

        if jarak < root.jarak:
            root.left = self.delete_node(root.left, jarak)

        elif jarak > root.jarak:
            root.right = self.delete_node(root.right, jarak)

        else:
            # Node tanpa child
            if root.left is None and root.right is None:
                return None

            # Node dengan 1 child
            elif root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # Node dengan 2 child
            temp = self.find_min(root.right)

            root.lokasi = temp.lokasi
            root.jarak = temp.jarak

            root.right = self.delete_node(root.right, temp.jarak)

        return root

    def delete(self, jarak):
        self.root = self.delete_node(self.root, jarak)


def main():
    gps = BSTNavigasiGPS()

    pilih = 0

    while pilih != 7:
        print("\n=== SISTEM NAVIGASI GPS (BST) ===")
        print("1. Tambah Lokasi")
        print("2. Cari Lokasi")
        print("3. Tampilkan Semua Lokasi")
        print("4. Lokasi Terdekat")
        print("5. Lokasi Terjauh")
        print("6. Hapus Lokasi")
        print("7. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka!")
            continue

        # Tambah lokasi
        if pilih == 1:
            lokasi = input("Masukkan nama lokasi: ")

            try:
                jarak = int(input("Masukkan jarak lokasi (KM): "))

                gps.insert(lokasi, jarak)

                print(f"Lokasi {lokasi} berhasil ditambahkan")

            except ValueError:
                print("Jarak harus angka!")

        # Cari lokasi
        elif pilih == 2:
            try:
                jarak = int(input("Masukkan jarak lokasi yang dicari: "))

                hasil = gps.search(gps.root, jarak)

                if hasil:
                    print("\nLokasi ditemukan:")
                    print(f"{hasil.lokasi} - {hasil.jarak} KM")

                else:
                    print("Lokasi tidak ditemukan")

            except ValueError:
                print("Input harus angka!")

        # Tampilkan semua lokasi
        elif pilih == 3:
            print("\nDaftar Lokasi:")

            if gps.root is None:
                print("Belum ada lokasi")

            else:
                gps.inorder(gps.root)

        # Lokasi terdekat
        elif pilih == 4:
            hasil = gps.find_min(gps.root)

            if hasil:
                print("\nLokasi Terdekat:")
                print(f"{hasil.lokasi} - {hasil.jarak} KM")

            else:
                print("Belum ada data lokasi")

        # Lokasi terjauh
        elif pilih == 5:
            hasil = gps.find_max(gps.root)

            if hasil:
                print("\nLokasi Terjauh:")
                print(f"{hasil.lokasi} - {hasil.jarak} KM")

            else:
                print("Belum ada data lokasi")

        # Hapus lokasi
        elif pilih == 6:
            try:
                jarak = int(input("Masukkan jarak lokasi yang ingin dihapus: "))

                gps.delete(jarak)

                print("Lokasi berhasil dihapus")

            except ValueError:
                print("Input harus angka!")

        # Keluar
        elif pilih == 7:
            print("Program selesai")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()