APLIKASI NAVIGASI  GPS

Kode ini merupakan implementasi Binary Search Tree (BST) pada sistem navigasi GPS sederhana menggunakan Python. Program digunakan untuk menyimpan dan mengelola data lokasi berdasarkan jarak tertentu. Pengguna dapat menambahkan lokasi, mencari lokasi berdasarkan jarak, menampilkan seluruh lokasi secara berurutan dari yang terdekat hingga terjauh, melihat lokasi paling dekat dan paling jauh, serta menghapus lokasi dari sistem. Penggunaan struktur data BST membuat proses pencarian, penambahan, dan penghapusan data menjadi lebih cepat, teratur, dan efisien dibandingkan penyimpanan data biasa.


<img width="407" height="162" alt="Screenshot 2026-05-25 180522" src="https://github.com/user-attachments/assets/0a0f93f9-537d-4d29-ad1e-cfa1d8afd002" />

Kode tersebut digunakan untuk membuat class Node pada Binary Search Tree (BST). Setiap node berfungsi sebagai tempat penyimpanan data lokasi dan jarak pada sistem navigasi GPS. Variabel lokasi digunakan untuk menyimpan nama tempat, sedangkan jarak digunakan untuk menyimpan jarak lokasi tersebut. Selain itu, left dan right digunakan untuk menghubungkan node ke cabang kiri dan kanan pada BST.

<img width="634" height="638" alt="Screenshot 2026-05-25 180824" src="https://github.com/user-attachments/assets/d4ed0097-f431-40ef-938d-adbe02961f10" />
<img width="607" height="684" alt="Screenshot 2026-05-25 180835" src="https://github.com/user-attachments/assets/b00602a8-0a56-4177-bf98-14a3a968b7d8" />
<img width="623" height="787" alt="Screenshot 2026-05-25 180848" src="https://github.com/user-attachments/assets/6e8e3431-0e4c-471b-8af2-ce1075d41414" />

Kode tersebut merupakan class utama dalam program Binary Search Tree (BST) yang digunakan untuk sistem navigasi GPS sederhana. Class BSTNavigasiGPS berfungsi untuk mengelola seluruh data lokasi dan jarak yang disimpan di dalam tree. Fungsi insert_node digunakan untuk menambahkan lokasi baru ke dalam BST berdasarkan nilai jarak sehingga data tersusun secara teratur. Fungsi inorder digunakan untuk menampilkan seluruh lokasi secara berurutan dari jarak terdekat hingga terjauh. Fungsi search digunakan untuk mencari lokasi tertentu berdasarkan jarak yang dimasukkan pengguna. Fungsi find_min digunakan untuk menemukan lokasi dengan jarak paling dekat, sedangkan find_max digunakan untuk menemukan lokasi dengan jarak paling jauh. Selain itu, terdapat fungsi delete_node yang digunakan untuk menghapus data lokasi dari BST tanpa merusak struktur tree yang sudah ada. Dengan menggunakan BST, proses penyimpanan, pencarian, penampilan, dan penghapusan data lokasi menjadi lebih cepat, efisien, dan mudah diatur dalam sistem navigasi GPS sederhana.

<img width="265" height="47" alt="Screenshot 2026-05-25 181212" src="https://github.com/user-attachments/assets/8d8f0528-4b77-45a6-a92d-f52ef00af327" />

Kode tersebut merupakan fungsi utama program yang digunakan untuk menjalankan sistem navigasi GPS berbasis Binary Search Tree (BST). Pada bagian gps = BSTNavigasiGPS(), program membuat objek baru dari class BSTNavigasiGPS yang nantinya digunakan untuk menyimpan, mencari, menampilkan, dan menghapus data lokasi dalam BST.

<img width="549" height="594" alt="Screenshot 2026-05-25 181327" src="https://github.com/user-attachments/assets/099cb5d9-d542-4b95-aa11-4d77410d52e2" />
<img width="578" height="701" alt="Screenshot 2026-05-25 181338" src="https://github.com/user-attachments/assets/cf48981f-fc73-46ed-8796-4540a5193fad" />
<img width="561" height="566" alt="Screenshot 2026-05-25 181348" src="https://github.com/user-attachments/assets/f2446055-bf4a-430c-a5f3-37e50370fb36" />


Kode tersebut digunakan untuk membuat menu utama pada sistem navigasi GPS berbasis Binary Search Tree (BST). Program akan terus berjalan menggunakan perulangan while sampai pengguna memilih menu keluar. Pada bagian ini, pengguna dapat memilih berbagai fitur seperti menambahkan lokasi, mencari lokasi berdasarkan jarak, menampilkan seluruh lokasi, melihat lokasi terdekat dan terjauh, serta menghapus lokasi tertentu. Program juga menggunakan try dan except untuk menangani kesalahan input agar tidak terjadi error ketika pengguna memasukkan data yang bukan angka. Dengan adanya menu ini, pengguna dapat berinteraksi langsung dengan sistem BST secara lebih mudah dan teratur.

<img width="271" height="79" alt="Screenshot 2026-05-25 181459" src="https://github.com/user-attachments/assets/b9ae8eb1-2396-4c2b-910e-183687be47fb" />

Kode tersebut digunakan untuk menjalankan fungsi utama program. Kondisi `if __name__ == "__main__":` memastikan bahwa fungsi `main()` hanya akan dijalankan ketika file Python dieksekusi secara langsung, bukan saat file diimport ke program lain. Bagian ini berfungsi sebagai titik awal agar seluruh sistem navigasi GPS berbasis BST dapat berjalan.
https://youtu.be/YxO_UC0YGnk
