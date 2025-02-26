#include "Aksesoris.cpp"

class Baju : public Aksesoris {
    private:
        string untuk;
        string size;
        string merk;
    
    public:
        Baju(int id, const string& nama, double harga, int stok,
             const string& jenis, const string& bahan, const string& warna,
             const string& untuk, const string& size, const string& merk)
            : Aksesoris(id, nama, harga, stok, jenis, bahan, warna) {
            this->untuk = untuk;
            this->size = size;
            this->merk = merk;
        }
    
        string getUntuk() const { return this->untuk; }
        string getSize() const { return this->size; }
        string getMerk() const { return this->merk; }
    
        vector<string> getColumnHeaders() const { 
            vector<string> headers = Aksesoris::getColumnHeaders();
            headers.push_back("UNTUK");
            headers.push_back("SIZE");
            headers.push_back("MERK");
            return headers;
        }
    
        vector<string> getData() const { 
            vector<string> data = Aksesoris::getData();
            data.push_back(this->untuk);
            data.push_back(this->size);
            data.push_back(this->merk);
            return data;
        }
    };
    