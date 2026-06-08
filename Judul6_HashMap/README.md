*Kamus Bahasa Digital*

Program ini merupakan implementasi struktur data HashMap menggunakan metode Separate Chaining untuk menangani collision (dua atau lebih data memiliki indeks hash yang sama). Program digunakan untuk menyimpan, mencari, memperbarui, menampilkan, dan menghapus data secara efisien. Dengan adanya fitur menu interaktif, pengguna dapat mengelola data dengan mudah, melihat isi setiap bucket, mengetahui jumlah data yang tersimpan, serta menghitung load factor untuk mengetahui tingkat pemakaian hash table. Program ini cocok digunakan sebagai simulasi sistem penyimpanan data seperti kamus digital, data mahasiswa, inventaris barang, atau database sederhana.


<img width="401" height="157" alt="Screenshot 2026-06-08 194827" src="https://github.com/user-attachments/assets/d4eb2ba7-4920-4f30-8f14-d5cc0a7c9e9e" />

Kelas Node digunakan untuk membuat satu simpul pada linked list yang digunakan dalam metode Separate Chaining. Setiap simpul menyimpan key sebagai kunci data, value sebagai nilai data, dan next sebagai penunjuk ke simpul berikutnya. Struktur ini memungkinkan beberapa data yang memiliki indeks hash yang sama disimpan dalam satu bucket secara berantai sehingga collision dapat ditangani dengan baik.


<img width="633" height="679" alt="Screenshot 2026-06-08 195122" src="https://github.com/user-attachments/assets/47eb424a-61c6-4f54-9e46-a2e8cd4a9cf4" />

Kelas HashMapSeparateChaining digunakan untuk mengelola penyimpanan data menggunakan struktur hash table dengan metode Separate Chaining. Konstruktor menginisialisasi ukuran tabel, membuat bucket kosong, dan menghitung jumlah data yang tersimpan. Fungsi `hash_function()` digunakan untuk menentukan indeks penyimpanan berdasarkan nilai key. Fungsi `insert()` berfungsi menambahkan data baru ke dalam hash table atau memperbarui value jika key sudah ada. Jika terjadi collision, data baru akan disimpan pada awal linked list di bucket yang sama sehingga semua data tetap dapat disimpan dengan baik.


<img width="529" height="772" alt="Screenshot 2026-06-08 195314" src="https://github.com/user-attachments/assets/2f27bfe2-bd97-41fe-84d9-e4e1bc7957e3" />

Fungsi `search()` digunakan untuk mencari data berdasarkan key. Fungsi ini menghitung indeks hash dari key, kemudian menelusuri linked list pada bucket tersebut hingga data ditemukan. Jika key sesuai, fungsi akan mengembalikan node yang berisi data tersebut, sedangkan jika tidak ditemukan fungsi akan mengembalikan `None`.

Fungsi `remove_key()` digunakan untuk menghapus data berdasarkan key. Fungsi ini mencari data pada bucket yang sesuai, kemudian menghapus node dari linked list dengan menghubungkan node sebelumnya ke node berikutnya. Jika data berhasil dihapus, jumlah data akan dikurangi dan program menampilkan pesan bahwa data berhasil dihapus. Jika key tidak ditemukan, program akan menampilkan pesan bahwa data tidak ditemukan.


<img width="682" height="412" alt="Screenshot 2026-06-08 195430" src="https://github.com/user-attachments/assets/10a28b08-6c1e-4393-a8e0-c1a082e7a37c" />

Fungsi `display()` digunakan untuk menampilkan seluruh isi hash table. Fungsi ini akan menelusuri setiap bucket dalam tabel dan menampilkan semua data yang tersimpan pada bucket tersebut. Jika terdapat beberapa data dalam satu bucket akibat collision, data akan ditampilkan secara berurutan mengikuti linked list. Tampilan ini membantu pengguna melihat bagaimana data didistribusikan dan disimpan dalam hash table menggunakan metode Separate Chaining.


<img width="627" height="759" alt="Screenshot 2026-06-08 195554" src="https://github.com/user-attachments/assets/7b95796c-e7ee-4fa4-9602-df228fd10f69" />

Fungsi `total_data()` digunakan untuk menampilkan jumlah seluruh data yang tersimpan di dalam hash table berdasarkan nilai variabel `count`.

Fungsi `load_factor()` digunakan untuk menghitung dan menampilkan nilai load factor, yaitu perbandingan antara jumlah data yang tersimpan dengan ukuran hash table. Nilai ini digunakan untuk mengetahui tingkat pemakaian tabel hash.

Fungsi `tampil_bucket()` digunakan untuk menampilkan isi dari bucket tertentu berdasarkan indeks yang dipilih. Jika indeks tidak valid, program akan memberikan pesan kesalahan. Jika bucket kosong, program akan menampilkan keterangan bahwa bucket tersebut kosong.

Fungsi `clear()` digunakan untuk menghapus seluruh data yang ada di dalam hash table dengan mengosongkan semua bucket dan mengatur kembali jumlah data menjadi nol sehingga hash table dapat digunakan kembali dari kondisi awal.


<img width="467" height="435" alt="Screenshot 2026-06-08 195654" src="https://github.com/user-attachments/assets/f3f928b9-7d49-42a8-9afc-c3f03b3cc001" />

Fungsi `menu()` digunakan sebagai antarmuka utama program yang menyediakan menu interaktif bagi pengguna. Pada fungsi ini dibuat objek `HashMapSeparateChaining` untuk menyimpan data, kemudian program akan terus berjalan menggunakan perulangan `while True` hingga pengguna memilih keluar. Menu yang ditampilkan berisi berbagai pilihan seperti menambah data, mencari data, menghapus data, menampilkan seluruh isi hash table, melihat jumlah data, menghitung load factor, menampilkan isi bucket tertentu, menghapus semua data, dan mengakhiri program.


<img width="436" height="879" alt="Screenshot 2026-06-08 195750" src="https://github.com/user-attachments/assets/4cccac4f-afd3-4138-9a5a-c3f5e5b3184e" />

Bagian kode ini digunakan untuk memproses pilihan menu yang dimasukkan oleh pengguna. Program akan membaca input menu, kemudian menjalankan fungsi yang sesuai, seperti menambahkan data, mencari data berdasarkan ID, menghapus data, menampilkan seluruh isi hash table, menampilkan jumlah data, menghitung load factor, melihat isi bucket tertentu, atau menghapus semua data. Jika pengguna memilih menu keluar, program akan berhenti. Apabila pilihan yang dimasukkan tidak sesuai dengan menu yang tersedia, program akan menampilkan pesan bahwa pilihan tidak valid.


<img width="303" height="57" alt="Screenshot 2026-06-08 195840" src="https://github.com/user-attachments/assets/735ab5da-2774-49fc-80e9-524f21e83d9d" />

Bagian kode ini berfungsi sebagai titik awal eksekusi program. Pernyataan `if __name__ == "__main__":` memastikan bahwa fungsi `menu()` hanya akan dijalankan ketika file dieksekusi secara langsung. Jika file tersebut diimpor ke program lain sebagai modul, fungsi `menu()` tidak akan dijalankan secara otomatis.

https://youtu.be/IuQllnYO6Q0
