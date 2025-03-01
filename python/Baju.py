from Aksesoris import Aksesoris

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