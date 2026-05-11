PROGRAM MENCARI FILE DI FOLDER


<img width="517" height="319" alt="Screenshot 2026-05-11 113654" src="https://github.com/user-attachments/assets/7ee74b5f-ac27-4086-a746-8ff4ae180e5e" />
Fungsi sequential_search() digunakan untuk mencari data secara berurutan dari awal sampai akhir list. Variabel i dipakai sebagai indeks untuk mengecek setiap data, sedangkan posisi digunakan untuk menyimpan letak data yang ditemukan. Perulangan while akan memeriksa data satu per satu. Jika data sama dengan target yang dicari, maka indeks data tersebut disimpan ke dalam list posisi. Setelah semua data selesai dicek, fungsi akan mengembalikan posisi data yang ditemukan.

<img width="467" height="147" alt="Screenshot 2026-05-11 114012" src="https://github.com/user-attachments/assets/8fb7da3d-1e94-40b7-aafe-d11a363ba78c" />
Fungsi tampilkan_data() digunakan untuk menampilkan seluruh data file yang ada di dalam list. Perintah print() digunakan untuk menampilkan judul daftar file. Perulangan for digunakan untuk mengulang semua data berdasarkan jumlah data dalam list. Nilai i digunakan sebagai indeks untuk mengambil data dari list. Bagian i + 1 digunakan agar nomor urut dimulai dari 1, bukan dari 0. Sedangkan data[i] digunakan untuk menampilkan isi data sesuai indeksnya.

<img width="511" height="120" alt="Screenshot 2026-05-11 114133" src="https://github.com/user-attachments/assets/c76e00d7-22a4-4186-be00-ae28138e6e59" />
Fungsi tambah_file() digunakan untuk menambahkan file baru ke dalam list data. Perintah input() digunakan untuk meminta pengguna memasukkan nama file baru. Data yang dimasukkan disimpan ke dalam variabel nama. Method append() digunakan untuk menambahkan nama file tersebut ke akhir list data. Setelah file berhasil ditambahkan, program menampilkan pesan bahwa file berhasil ditambahkan.

<img width="651" height="239" alt="Screenshot 2026-05-11 114529" src="https://github.com/user-attachments/assets/7d4f42c5-b926-419a-ad9e-fb035ba4efc1" />
Fungsi hapus_file() digunakan untuk menghapus file dari dalam list data. Perintah input() digunakan untuk meminta pengguna memasukkan nama file yang ingin dihapus. Kondisi if digunakan untuk mengecek apakah nama file tersebut ada di dalam list data. Jika file ditemukan, method remove() digunakan untuk menghapus file dari list, lalu program menampilkan pesan bahwa file berhasil dihapus. Jika file tidak ada, program akan menampilkan pesan bahwa file tidak ditemukan.

<img width="376" height="533" alt="Screenshot 2026-05-11 114657" src="https://github.com/user-attachments/assets/7176c44a-4064-464f-a342-de1970d03a26" />
Fungsi main() merupakan fungsi utama dalam program. Di dalam fungsi ini terdapat variabel data yang berisi kumpulan nama file dalam bentuk list. Data tersebut digunakan sebagai sumber data untuk proses pencarian, penambahan, penghapusan, dan penampilan file pada program. Setiap elemen dalam list merupakan nama file yang tersimpan di dalam folder.

<img width="490" height="841" alt="Screenshot 2026-05-11 114811" src="https://github.com/user-attachments/assets/ab7ef892-c4aa-410a-8cc5-0a416723d19d" />
Perulangan while True digunakan agar menu program terus berjalan sampai pengguna memilih keluar. Perintah print() digunakan untuk menampilkan daftar menu program, seperti menampilkan file, mencari file, menambah file, menghapus file, dan keluar dari program. Input pilihan disimpan ke dalam variabel pilihan.

Kondisi if dan elif digunakan untuk menjalankan fitur sesuai pilihan pengguna. Jika pengguna memilih “1”, program akan memanggil fungsi tampilkan_data() untuk menampilkan daftar file. Jika memilih “2”, program meminta nama file yang ingin dicari lalu menjalankan fungsi sequential_search() untuk mencari file secara berurutan. Jika file ditemukan, program menampilkan posisi dan jumlah file yang ditemukan. Jika tidak ditemukan, program menampilkan pesan bahwa file tidak ditemukan.

Jika pengguna memilih “3”, program menjalankan fungsi tambah_file() untuk menambahkan file baru. Jika memilih “4”, program menjalankan fungsi hapus_file() untuk menghapus file. Jika memilih “5”, program menampilkan pesan selesai lalu menghentikan perulangan menggunakan break. Sedangkan else digunakan untuk menampilkan pesan jika pilihan menu tidak valid.

<img width="320" height="61" alt="Screenshot 2026-05-11 114917" src="https://github.com/user-attachments/assets/1dcd54cf-7adc-4c1a-83ba-2dd63d0fd472" />
Kode if name == "main": digunakan untuk memastikan bahwa fungsi main() hanya dijalankan saat file program dijalankan secara langsung. Perintah main() digunakan untuk memulai seluruh program utama. Jika file hanya diimpor ke program lain, maka fungsi main() tidak akan otomatis dijalankan.
