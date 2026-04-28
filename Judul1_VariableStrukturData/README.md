PROGRAM KERETA API

Program kereta api ini menggunakan konsep linked list, di mana setiap gerbong adalah node yang saling terhubung ke gerbong berikutnya. Terdapat penunjuk kepala sebagai lokomotif atau bagian paling depan.
Saat user memilih menu, program menjalankan fungsi sesuai input. Menambah gerbong akan menyambungkan node baru ke akhir atau posisi tertentu. Menghapus gerbong dilakukan dengan memutus dan menyambung kembali node di sekitarnya tanpa menggeser data lain. Ganti lokomotif cukup mengubah data pada node pertama.
Fungsi tampilkan akan menelusuri seluruh gerbong dari depan ke belakang. Program berjalan terus dalam loop sampai user memilih keluar.

<img width="337" height="135" alt="Screenshot 2026-04-26 171059" src="https://github.com/user-attachments/assets/5a13a262-bce2-44cb-8c2c-266bf58bf551" />
Kode ini berfungsi untuk membuat satu gerbong (node) dalam linked list yang menyimpan nama gerbong dan memiliki penunjuk ke gerbong berikutnya (next)

<img width="320" height="84" alt="Screenshot 2026-04-26 171424" src="https://github.com/user-attachments/assets/a17c338e-c0b8-4ed3-be2a-01bcc78a9cc9" />
Kode ini berfungsi untuk membuat struktur utama kereta (linked list) dan menginisialisasi kepala sebagai penunjuk ke gerbong pertama (lokomotif), yang awalnya kosong (None).

<img width="504" height="270" alt="Screenshot 2026-04-26 171627" src="https://github.com/user-attachments/assets/3c90a59c-0e9e-485e-9218-133a3ac3932a" />
Kode ini berfungsi untuk menambahkan gerbong baru ke dalam rangkaian kereta. Pertama dibuat objek gerbong baru dari nama yang diberikan. Jika kereta masih kosong, gerbong tersebut langsung menjadi kepala. Jika sudah ada gerbong, program akan menelusuri dari kepala sampai ke gerbong terakhir, lalu menghubungkan gerbong baru di bagian paling akhir.

<img width="499" height="467" alt="Screenshot 2026-04-26 172050" src="https://github.com/user-attachments/assets/3a92a07d-e2f1-41b1-955e-1ef8e9604eb4" />
Kode ini berfungsi untuk menambahkan gerbong baru pada posisi tertentu dalam rangkaian kereta. Jika posisi yang dimasukkan adalah 0, maka gerbong baru akan ditempatkan di depan dan menjadi kepala. Jika bukan, program akan menelusuri hingga posisi sebelum titik penyisipan, lalu menghubungkan gerbong baru di antara gerbong sebelumnya dan berikutnya dengan mengatur pointer next. Jika posisi tidak valid, program akan menampilkan pesan kesalahan.

<img width="580" height="475" alt="Screenshot 2026-04-26 172253" src="https://github.com/user-attachments/assets/3d64a177-3197-4d6f-8146-04312c20db78" />
Kode ini berfungsi untuk menghapus gerbong berdasarkan nama dari rangkaian kereta. Program akan mulai dari kepala dan mengecek apakah gerbong pertama yang ingin dihapus, jika iya maka kepala dipindahkan ke gerbong berikutnya. Jika bukan, program akan menelusuri sampai menemukan gerbong yang sesuai sambil menyimpan gerbong sebelumnya. Setelah ditemukan, hubungan akan diputus dengan menghubungkan gerbong sebelumnya langsung ke gerbong setelahnya. Jika gerbong tidak ditemukan, program akan menampilkan pesan kesalahan.

<img width="463" height="167" alt="Screenshot 2026-04-26 172407" src="https://github.com/user-attachments/assets/dba5f243-9098-4d17-8a03-026fac982fd1" />
Kode ini berfungsi untuk mengganti nama lokomotif pada rangkaian kereta. Program akan mengecek terlebih dahulu apakah kereta kosong, jika kosong maka akan menampilkan pesan. Jika tidak, program langsung mengubah nilai nama pada gerbong pertama tanpa mengubah struktur rangkaian.

<img width="554" height="271" alt="Screenshot 2026-04-26 172508" src="https://github.com/user-attachments/assets/df32f7a0-6619-43fd-aea0-500d5cc4e9da" />
Kode ini berfungsi untuk menampilkan seluruh rangkaian gerbong dalam kereta. Program akan mulai dari kepala, lalu menelusuri setiap gerbong satu per satu hingga ke akhir. Jika kereta kosong, akan menampilkan pesan. Jika ada isi, setiap nama gerbong akan ditampilkan secara berurutan dengan tanda panah sebagai penghubung sampai mencapai akhir yang ditandai dengan None.

<img width="290" height="31" alt="Screenshot 2026-04-26 172647" src="https://github.com/user-attachments/assets/0eecacba-3f5e-4d84-8bff-309ca3b42e37" />
Kode ini berfungsi untuk membuat sebuah objek kereta api dari class KeretaApi, yang nantinya digunakan untuk menjalankan semua operasi seperti menambah, menghapus, dan menampilkan gerbong.

<img width="566" height="842" alt="Screenshot 2026-04-26 172931" src="https://github.com/user-attachments/assets/84252150-3366-42af-90f6-349752f4b2f5" />
Kode ini berfungsi sebagai menu utama program yang berjalan terus menerus untuk menerima input dari user. Program akan menampilkan pilihan menu, lalu membaca input user untuk menentukan aksi yang akan dijalankan seperti menambah gerbong, menyisipkan di posisi tertentu, menghapus gerbong, mengganti lokomotif, atau menampilkan rangkaian. Setiap pilihan akan memanggil fungsi yang sesuai pada objek kereta. Jika user memilih keluar, perulangan akan dihentikan dan program selesai.

https://youtu.be/FaJ73NwvEa4
