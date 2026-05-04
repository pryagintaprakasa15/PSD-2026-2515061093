PROGRAM MENGURUTKAN KODE BUKU DIPERPUSTAKAAN

Program ini digunakan untuk mengurutkan kode buku dengan menggunakan struktur data list dan algoritma selection sort. Cara kerjanya adalah mencari data terkecil dari bagian yang belum terurut, lalu menukarnya ke posisi yang seharusnya sampai semua data tersusun rapi. Fungsi tukar dipakai untuk menukar dua data agar proses sorting lebih mudah. Di dalam main, program meminta jumlah buku lalu menerima input kode buku satu per satu dengan validasi agar tidak kosong. Setelah itu data ditampilkan sebelum dan sesudah diurutkan. Selanjutnya program masuk ke dalam perulangan menu, di mana user bisa menambah atau menghapus data. Setiap kali ada perubahan, data akan langsung diurutkan kembali agar tetap rapi. Program akan terus berjalan sampai user memilih untuk selesai.

<img width="451" height="135" alt="Screenshot 2026-05-04 094941" src="https://github.com/user-attachments/assets/02d85a26-6c13-4a9d-8bc1-840c8bc5970a" />
Fungsi ini digunakan untuk menukar posisi dua data dalam list berdasarkan indeksnya. Nilai pada indeks i disimpan sementara ke variabel temp, lalu nilai pada indeks j dipindahkan ke posisi i, dan terakhir nilai yang ada di temp dimasukkan ke posisi j sehingga kedua data berhasil ditukar.

<img width="401" height="244" alt="Screenshot 2026-05-04 095252" src="https://github.com/user-attachments/assets/a398bfcb-7100-4646-a401-9322072899a6" />
Fungsi ini digunakan untuk mengurutkan data dalam list menggunakan metode selection sort. Program akan mengulang dari indeks awal sampai sebelum terakhir, lalu menganggap posisi i sebagai posisi dengan nilai terkecil sementara. Setelah itu, dilakukan pencarian ke sisa data di sebelah kanan untuk menemukan nilai yang lebih kecil. Jika ditemukan, posisi tersebut disimpan di variabel pos. Setelah pencarian selesai, jika pos tidak sama dengan i, maka data pada kedua posisi tersebut ditukar menggunakan fungsi tukar. Proses ini terus dilakukan sampai semua data terurut.

<img width="662" height="164" alt="Screenshot 2026-05-04 095436" src="https://github.com/user-attachments/assets/3946184c-f52a-4a28-9843-1e591506caac" />
Bagian ini adalah awal dari fungsi utama program. Program mencoba meminta input jumlah buku dari user dan mengubahnya menjadi angka. Jika input yang dimasukkan bukan angka, maka akan terjadi error dan langsung ditangkap oleh except, sehingga program menampilkan pesan bahwa input tidak valid lalu berhenti dengan return.

<img width="541" height="291" alt="Screenshot 2026-05-04 095517" src="https://github.com/user-attachments/assets/10a68dac-bb05-458e-ba3d-9ef86c811ea3" />
Bagian ini digunakan untuk menampung dan mengisi data kode buku ke dalam list. Pertama dibuat list kosong arr, lalu program meminta user memasukkan kode buku sebanyak n kali. Di dalam perulangan, digunakan while True untuk memastikan input tidak kosong. Jika user memasukkan data kosong, program akan meminta input ulang. Jika valid, kode buku akan ditambahkan ke dalam arr dan perulangan lanjut ke data berikutnya.

<img width="501" height="106" alt="Screenshot 2026-05-04 095618" src="https://github.com/user-attachments/assets/a72cba7d-b94e-43d3-8a1b-641312c0afb1" />
Bagian ini menampilkan data buku sebelum diurutkan, lalu memanggil fungsi selection_sort untuk mengurutkan isi list arr. Setelah proses pengurutan selesai, program menampilkan kembali data yang sudah dalam keadaan terurut.

<img width="477" height="148" alt="Screenshot 2026-05-04 095757" src="https://github.com/user-attachments/assets/2ed80fe5-3ecb-4f7d-aa95-3f10d24e1c0e" />
Bagian ini digunakan untuk menampilkan menu pilihan secara berulang menggunakan perulangan tanpa batas. Program akan terus mencetak pilihan aksi yaitu menambah data buku, menghapus data buku, atau selesai, sampai nanti ada kondisi yang menghentikan perulangan.

<img width="456" height="20" alt="Screenshot 2026-05-04 095936" src="https://github.com/user-attachments/assets/1b9a3943-e945-4504-9bc9-42dcc79676d2" />
Baris ini digunakan untuk menerima input dari user terkait pilihan menu yang sudah ditampilkan sebelumnya. Nilai yang dimasukkan akan disimpan ke variabel pilihan dan nantinya dipakai untuk menentukan aksi yang dijalankan oleh program.

<img width="615" height="140" alt="Screenshot 2026-05-04 100019" src="https://github.com/user-attachments/assets/d0380f8e-650c-4f5d-a66f-73b38a50586f" />
Bagian ini dijalankan ketika user memilih opsi 1. Program akan meminta input kode buku baru, lalu menambahkannya ke dalam list arr. Setelah itu, seluruh data diurutkan kembali menggunakan selection_sort agar tetap rapi, kemudian hasilnya ditampilkan ke layar.

<img width="644" height="230" alt="Screenshot 2026-05-04 100117" src="https://github.com/user-attachments/assets/17aad874-4e00-435a-a93f-5ba6c7fbbf90" />
Bagian ini dijalankan ketika user memilih opsi 2. Program akan meminta kode buku yang ingin dihapus, lalu mengecek apakah data tersebut ada di dalam list. Jika ada, data akan dihapus dari arr, kemudian list diurutkan kembali agar tetap rapi, dan hasilnya ditampilkan. Jika kode buku tidak ditemukan, program akan menampilkan pesan bahwa data tidak ada.

<img width="450" height="142" alt="Screenshot 2026-05-04 100211" src="https://github.com/user-attachments/assets/8bd2f882-11cb-44ec-9593-5d2f628c934e" />
Bagian ini dijalankan ketika user memilih opsi 3. Program akan menampilkan pesan bahwa program selesai, lalu menghentikan perulangan dengan break sehingga program berhenti. Jika input yang dimasukkan tidak sesuai pilihan yang tersedia, maka program akan menampilkan pesan bahwa pilihan tidak valid.

<img width="306" height="59" alt="Screenshot 2026-05-04 100254" src="https://github.com/user-attachments/assets/ad39afbb-ddc1-4f7a-972f-59db3959a68d" />
Bagian ini digunakan untuk memastikan bahwa fungsi main hanya dijalankan ketika file program ini dijalankan langsung, bukan saat diimpor ke file lain. Jika kondisi tersebut terpenuhi, maka program akan mulai menjalankan fungsi main sebagai titik awal eksekusi.
