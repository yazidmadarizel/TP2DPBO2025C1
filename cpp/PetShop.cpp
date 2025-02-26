#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class PetShop {
private:
    int id;
    string nama_produk;
    double harga_produk;
    int stok_produk;

public:
    PetShop(int id, const string& nama, double harga, int stok) {
        this->id = id;
        this->nama_produk = nama;
        this->harga_produk = harga;
        this->stok_produk = stok;
    }

    int getId() const { return this->id; }
    string getNama() const { return this->nama_produk; }
    double getHarga() const { return this->harga_produk; }
    int getStok() const { return this->stok_produk; }

    static vector<string> getColumnHeaders() {
        return {"ID", "NAMA PRODUK", "HARGA", "STOK"};
    }

    vector<string> getData() const {
        return {
            to_string(this->id),
            this->nama_produk,
            "Rp" + to_string(this->harga_produk),
            to_string(this->stok_produk)
        };
    }
};