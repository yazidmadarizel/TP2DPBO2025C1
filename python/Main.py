class PetShop:
    def __init__(self, id, nama, harga, stok):
        self.id = id
        self.nama_produk = nama
        self.harga_produk = harga
        self.stok_produk = stok

    def get_id(self):
        return self.id

    def get_nama(self):
        return self.nama_produk

    def get_harga(self):
        return self.harga_produk

    def get_stok(self):
        return self.stok_produk

    @staticmethod
    def get_column_headers():
        return ["ID", "NAMA PRODUK", "HARGA", "STOK"]

    def get_data(self):
        return [
            str(self.id),
            self.nama_produk,
            f"Rp{self.harga_produk}",
            str(self.stok_produk)
        ]


class Aksesoris(PetShop):
    def __init__(self, id, nama, harga, stok, jenis, bahan, warna):
        super().__init__(id, nama, harga, stok)
        self.jenis = jenis
        self.bahan = bahan
        self.warna = warna

    def get_jenis(self):
        return self.jenis

    def get_bahan(self):
        return self.bahan

    def get_warna(self):
        return self.warna

    def get_column_headers(self):
        headers = super().get_column_headers()
        headers.extend(["JENIS", "BAHAN", "WARNA"])
        return headers

    def get_data(self):
        data = super().get_data()
        data.extend([self.jenis, self.bahan, self.warna])
        return data


class Baju(Aksesoris):
    def __init__(self, id, nama, harga, stok, jenis, bahan, warna, untuk, size, merk):
        super().__init__(id, nama, harga, stok, jenis, bahan, warna)
        self.untuk = untuk
        self.size = size
        self.merk = merk

    def get_untuk(self):
        return self.untuk

    def get_size(self):
        return self.size

    def get_merk(self):
        return self.merk

    def get_column_headers(self):
        headers = super().get_column_headers()
        headers.extend(["UNTUK", "SIZE", "MERK"])
        return headers

    def get_data(self):
        data = super().get_data()
        data.extend([self.untuk, self.size, self.merk])
        return data


def display_table(headers, data):
    widths = [len(header) for header in headers]
    for row in data:
        for i, item in enumerate(row):
            if len(item) > widths[i]:
                widths[i] = len(item)

    print("+" + "+".join(["-" * (w + 2) for w in widths]) + "+")
    print("|" + "|".join([f" {headers[i].ljust(widths[i])} " for i in range(len(headers))]) + "|")
    print("+" + "+".join(["-" * (w + 2) for w in widths]) + "+")

    for row in data:
        print("|" + "|".join([f" {row[i].ljust(widths[i])} " if i < len(row) else " - ".ljust(widths[i]) for i in range(len(headers))]) + "|")

    print("+" + "+".join(["-" * (w + 2) for w in widths]) + "+")


def display_all_products(produk, aksesoris, baju):
    print("\n=== SEMUA PRODUK PETSHOP ===")
    
    headers = [
        "ID", "NAMA PRODUK", "HARGA", "STOK", "KATEGORI", 
        "JENIS", "BAHAN", "WARNA", "UNTUK", "SIZE", "MERK"
    ]
    
    all_data = []
    
    for p in produk:
        row = p.get_data()
        row.insert(4, "PetShop")
        while len(row) < len(headers):
            row.append("-")
        all_data.append(row)
    
    for a in aksesoris:
        row = a.get_data()
        row.insert(4, "Aksesoris")
        while len(row) < len(headers):
            row.append("-")
        all_data.append(row)
    
    for b in baju:
        row = b.get_data()
        row.insert(4, "Baju")
        while len(row) < len(headers):
            row.append("-")
        all_data.append(row)
    
    
    all_data.sort(key=lambda x: int(x[0]))  

    display_table(headers, all_data)

def get_next_id(produk, aksesoris, baju):
    max_id = 0
    for p in produk:
        if p.get_id() > max_id:
            max_id = p.get_id()
    for a in aksesoris:
        if a.get_id() > max_id:
            max_id = a.get_id()
    for b in baju:
        if b.get_id() > max_id:
            max_id = b.get_id()
    return max_id + 1


def add_new_product(produk, aksesoris, baju):
    print("\nJenis produk yang ingin ditambahkan:")
    print("1. Produk PetShop")
    print("2. Aksesoris")
    print("3. Baju")
    choice = input("Pilihan: ")

    if choice not in ["1", "2", "3"]:
        print("Input tidak valid.")
        return

    id = get_next_id(produk, aksesoris, baju)
    nama = input("Nama produk: ")
    harga = float(input("Harga produk: Rp"))
    stok = int(input("Stok produk: "))

    if choice == "1":
        produk.append(PetShop(id, nama, harga, stok))
        print("\nProduk PetShop berhasil ditambahkan!")
    elif choice == "2":
        jenis = input("Jenis aksesoris: ")
        bahan = input("Bahan: ")
        warna = input("Warna: ")
        aksesoris.append(Aksesoris(id, nama, harga, stok, jenis, bahan, warna))
        print("\nAksesoris berhasil ditambahkan!")
    elif choice == "3":
        jenis = input("Jenis pakaian: ")
        bahan = input("Bahan: ")
        warna = input("Warna: ")
        untuk = input("Untuk (hewan): ")
        size = input("Ukuran: ")
        merk = input("Merk: ")
        baju.append(Baju(id, nama, harga, stok, jenis, bahan, warna, untuk, size, merk))
        print("\nBaju berhasil ditambahkan!")


def main():
    produk = [
        PetShop(1, "Dog Food Premium", 85000, 25),
        PetShop(2, "Cat Litter Box", 120000, 10)
    ]

    aksesoris = [
        Aksesoris(3, "Cat Collar", 35000, 30, "Collar", "Leather", "Black"),
        Aksesoris(4, "Dog Leash", 65000, 15, "Leash", "Nylon", "Red")
    ]

    baju = [
        Baju(5, "Dog Raincoat", 150000, 8, "Coat", "Waterproof", "Yellow", "Anjing", "M", "PawStyle")
    ]

    while True:
        print("\n==== SISTEM MANAJEMEN PETSHOP ====")
        print("1. Tampilkan Semua Produk")
        print("2. Tambah Produk Baru")
        print("0. Keluar")
        choice = input("Pilihan: ")

        if choice == "1":
            display_all_products(produk, aksesoris, baju)
        elif choice == "2":
            add_new_product(produk, aksesoris, baju)
        elif choice == "0":
            print("Terima kasih telah menggunakan sistem manajemen PetShop.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()