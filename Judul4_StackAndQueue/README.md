SISTEM PARKIR MOBIL SATU JALUR

Kode ini adalah program simulasi parkiran mobil menggunakan struktur data stack berbasis array. Program menerapkan konsep LIFO (Last In First Out), sehingga mobil yang terakhir masuk akan menjadi mobil pertama yang keluar. Program memiliki fitur untuk menambah mobil, mengeluarkan mobil, melihat mobil terakhir, dan menampilkan seluruh isi parkiran melalui menu interaktif.

<img width="458" height="134" alt="Screenshot 2026-05-19 100412" src="https://github.com/user-attachments/assets/7890a5e8-0ca0-472f-bb63-2962895e0ba7" />

Kode tersebut merupakan constructor pada class ParkirStack yang digunakan untuk menginisialisasi stack parkiran. self.MAX = max_size digunakan untuk menentukan kapasitas maksimal parkiran, self.mobil = [None] * self.MAX digunakan untuk membuat array kosong sebagai tempat penyimpanan data mobil, dan self.top_idx = -1 menandakan bahwa stack masih kosong atau belum ada mobil yang masuk.

<img width="443" height="143" alt="Screenshot 2026-05-19 100627" src="https://github.com/user-attachments/assets/55a4248d-4450-4fd1-9ade-622dbe036c66" />

Fungsi is_empty digunakan untuk mengecek apakah stack kosong dengan memeriksa apakah nilai top_idx sama dengan -1. Sedangkan fungsi is_full digunakan untuk mengecek apakah stack penuh dengan memeriksa apakah top_idx sudah mencapai kapasitas maksimum stack.

<img width="541" height="226" alt="Screenshot 2026-05-19 100711" src="https://github.com/user-attachments/assets/b45eb908-875b-491f-92d6-7c0356ad95ea" />

Fungsi mobil_masuk digunakan untuk menambahkan mobil ke dalam parkiran. Program akan mengecek terlebih dahulu apakah parkiran penuh menggunakan fungsi is_full. Jika belum penuh, maka posisi top_idx akan bertambah satu dan data plat mobil akan disimpan ke dalam stack, lalu program menampilkan pesan bahwa mobil berhasil masuk parkiran.

<img width="670" height="220" alt="Screenshot 2026-05-19 100840" src="https://github.com/user-attachments/assets/8d101056-d958-4af6-b8c5-b3030c392220" />

Fungsi mobil_keluar digunakan untuk mengeluarkan mobil dari parkiran. Program akan mengecek terlebih dahulu apakah parkiran kosong menggunakan fungsi is_empty. Jika tidak kosong, maka mobil yang berada di posisi paling atas stack akan dikeluarkan dan nilai top_idx akan dikurangi satu.

<img width="613" height="162" alt="Screenshot 2026-05-19 100928" src="https://github.com/user-attachments/assets/d4ca91b2-fe9a-4177-92cc-15f39f97e837" />

Fungsi mobil_terakhir digunakan untuk menampilkan mobil yang berada di posisi paling atas stack atau mobil terakhir yang masuk ke parkiran. Program akan mengecek terlebih dahulu apakah parkiran kosong menggunakan fungsi is_empty. Jika tidak kosong, maka plat mobil terakhir akan ditampilkan.

<img width="553" height="229" alt="Screenshot 2026-05-19 101035" src="https://github.com/user-attachments/assets/4f197d5a-9f0f-4324-a930-3dfb58da09a0" />

Fungsi tampilkan_parkiran digunakan untuk menampilkan seluruh mobil yang ada di parkiran. Program akan mengecek terlebih dahulu apakah parkiran kosong menggunakan fungsi is_empty. Jika tidak kosong, maka data mobil akan ditampilkan dari posisi paling atas hingga paling bawah menggunakan perulangan for.

<img width="494" height="847" alt="Screenshot 2026-05-19 101157" src="https://github.com/user-attachments/assets/5e0e0868-895d-4f89-9b56-44ca8dcb6c00" />

Fungsi main digunakan sebagai program utama untuk menjalankan sistem parkir menggunakan struktur data stack. Pada fungsi ini dibuat objek parkir dari class ParkirStack, kemudian program menampilkan menu secara berulang menggunakan perulangan while sampai pengguna memilih opsi keluar.

Program menyediakan beberapa pilihan menu seperti menambah mobil ke parkiran, mengeluarkan mobil dari parkiran, melihat mobil terakhir yang masuk, dan menampilkan seluruh isi parkiran. Input dari pengguna akan diproses menggunakan percabangan if-elif sesuai dengan pilihan menu yang dipilih. Program juga menggunakan try-except untuk menangani kesalahan jika pengguna memasukkan input selain angka.

<img width="307" height="54" alt="Screenshot 2026-05-19 101302" src="https://github.com/user-attachments/assets/61458c54-3e5e-4650-bb74-951518a041db" />

Kode tersebut digunakan untuk menjalankan fungsi main sebagai program utama. Kondisi if **name** == "**main**" memastikan bahwa fungsi main hanya akan dijalankan ketika file program dieksekusi secara langsung, bukan saat file diimpor ke program lain.
