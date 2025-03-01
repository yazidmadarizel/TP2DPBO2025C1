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