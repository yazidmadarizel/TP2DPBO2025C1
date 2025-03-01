from PetShop import PetShop
from Aksesoris import Aksesoris
from Baju import Baju

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