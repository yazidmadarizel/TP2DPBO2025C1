from PetShop import PetShop

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