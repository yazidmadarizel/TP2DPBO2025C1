# TP2DPBO2025C1

Saya Yazid Madarizel dengan NIM 2305328 mengerjakan soal TP 2 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.


# Desain Program

Program terdiri dari tiga class utama yang memiliki hubungan inheritance (pewarisan), yaitu **PetShop** sebagai class induk, **Aksesoris** yang mewarisi PetShop, dan **Baju** yang mewarisi Aksesoris. Setiap class memiliki atribut dan metode untuk mengelola data produk sesuai jenisnya.

1. **PetShop (Class Induk)**
   * Atribut: id, nama_produk, harga_produk, stok_produk
   * Metode: get_id(), get_nama(), get_harga(), get_stok(), get_column_headers(), get_data()

2. **Aksesoris (Turunan dari PetShop)**
   * Mewarisi semua atribut dan metode PetShop
   * Atribut tambahan: jenis, bahan, warna
   * Metode tambahan: get_jenis(), get_bahan(), get_warna(), get_column_headers(), get_data()

3. **Baju (Turunan dari Aksesoris)**
   * Mewarisi semua atribut dan metode Aksesoris
   * Atribut tambahan: untuk, size, merk
   * Metode tambahan: get_untuk(), get_size(), get_merk(), get_column_headers(), get_data()

Program juga memiliki fungsi-fungsi pendukung seperti display_table() untuk menampilkan tabel, display_all_products() untuk menampilkan semua produk, get_next_id() untuk mendapatkan ID berikutnya, dan add_new_product() untuk menambahkan produk baru.

# Alur Program

1. **Inisialisasi Data**
   * Program dimulai dengan membuat beberapa data sampel untuk ketiga jenis produk (PetShop dasar, Aksesoris, dan Baju).

2. **Menampilkan Menu Utama**
   * User disajikan dengan menu pilihan untuk mengelola produk.
   * Pilihan meliputi: (1) Tampilkan Semua Produk, (2) Tambah Produk Baru, (0) Keluar.

3. **Menampilkan Semua Produk (Pilihan 1)**
   * Sistem menampilkan semua produk dalam bentuk tabel dengan kolom yang sesuai.
   * Produk diurutkan berdasarkan ID.
   * Tabel menampilkan semua atribut produk (ID, Nama, Harga, Stok, Kategori, dll).
   * Jika atribut tidak tersedia untuk jenis produk tertentu, ditampilkan tanda "-".

4. **Menambahkan Produk Baru (Pilihan 2)**
   * User memilih jenis produk yang ingin ditambahkan (PetShop, Aksesoris, atau Baju).
   * User memasukkan informasi dasar seperti nama, harga, dan stok.
   * Berdasarkan jenis produk, user diminta memasukkan informasi tambahan:
     - Aksesoris: jenis, bahan, warna
     - Baju: jenis, bahan, warna, untuk (hewan), size, merk
   * ID produk otomatis diberikan (ID tertinggi + 1).
   * Produk baru ditambahkan ke dalam daftar yang sesuai.

5. **Keluar dari Program (Pilihan 0)**
   * Program berhenti dengan menampilkan pesan "Terima kasih telah menggunakan sistem manajemen PetShop."

6. **Validasi Input**
   * Program memvalidasi input user untuk memastikan pilihan menu yang valid.
   * Untuk input numerik seperti harga dan stok, program mengharapkan nilai yang sesuai.

7. **Display Format**
   * Semua data ditampilkan dalam format tabel yang rapi dengan lebar kolom yang menyesuaikan isi.
   * Harga ditampilkan dengan format "Rp" di depannya.

# Desain Diagram

![Screenshot 2025-02-27 065158](https://github.com/user-attachments/assets/809139c5-76cd-46e9-8a7d-3fc05c75602b)
