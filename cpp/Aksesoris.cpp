#include "PetShop.cpp"

class Aksesoris : public PetShop {
    protected:
        string jenis;
        string bahan;
        string warna;
    
    public:
        Aksesoris(int id, const string& nama, double harga, int stok,
                  const string& jenis, const string& bahan, const string& warna)
            : PetShop(id, nama, harga, stok) {
            this->jenis = jenis;
            this->bahan = bahan;
            this->warna = warna;
        }
    
        string getJenis() const { return this->jenis; }
        string getBahan() const { return this->bahan; }
        string getWarna() const { return this->warna; }
    
        vector<string> getColumnHeaders() const { 
            vector<string> headers = PetShop::getColumnHeaders();
            headers.push_back("JENIS");
            headers.push_back("BAHAN");
            headers.push_back("WARNA");
            return headers;
        }
    
        vector<string> getData() const { 
            vector<string> data = PetShop::getData();
            data.push_back(this->jenis);
            data.push_back(this->bahan);
            data.push_back(this->warna);
            return data;
        }
    };