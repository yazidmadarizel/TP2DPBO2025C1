#include "Baju.cpp"


void displayTable(const vector<string>& headers, const vector<vector<string>>& data) {
    
    vector<int> widths(headers.size(), 0);
    for (size_t i = 0; i < headers.size(); ++i) {
        widths[i] = headers[i].size();
        for (const auto& row : data) {
            if (i < row.size() && row[i].size() > widths[i]) {
                widths[i] = row[i].size();
            }
        }
    }

    
    cout << "+";
    for (int w : widths) cout << string(w + 2, '-') << "+";
    cout << endl;

    cout << "|";
    for (size_t i = 0; i < headers.size(); ++i) {
        cout << " " << left << setw(widths[i]) << headers[i] << " |";
    }
    cout << endl;

    
    cout << "+";
    for (int w : widths) cout << string(w + 2, '-') << "+";
    cout << endl;

    
    for (const auto& row : data) {
        cout << "|";
        for (size_t i = 0; i < headers.size(); ++i) {
            cout << " " << left << setw(widths[i]) << (i < row.size() ? row[i] : "-") << " |";
        }
        cout << endl;
    }

    
    cout << "+";
    for (int w : widths) cout << string(w + 2, '-') << "+";
    cout << endl;
}


void displayAllProducts(const vector<PetShop>& produk, const vector<Aksesoris>& aksesoris, const vector<Baju>& baju) {
    cout << "\n=== SEMUA PRODUK PETSHOP ===" << endl;
    
    
    vector<string> headers = {
        "ID", "NAMA PRODUK", "HARGA", "STOK", "KATEGORI", 
        "JENIS", "BAHAN", "WARNA", "UNTUK", "SIZE", "MERK"
    };
    
    
    vector<vector<string>> allData;
    
    
    for (const auto& p : produk) {
        vector<string> row = p.getData();
        
        row.insert(row.begin() + 4, "PetShop");
        while (row.size() < headers.size()) {
            row.push_back("-");
        }
        allData.push_back(row);
    }
    
    
    for (const auto& a : aksesoris) {
        vector<string> row = a.getData();
        
        row.insert(row.begin() + 4, "Aksesoris");
        
        while (row.size() < headers.size()) {
            row.push_back("-");
        }
        allData.push_back(row);
    }
    
    
    for (const auto& b : baju) {
        vector<string> row = b.getData();
        
        row.insert(row.begin() + 4, "Baju");
        
        while (row.size() < headers.size()) {
            row.push_back("-");
        }
        allData.push_back(row);
    }
    
    
    sort(allData.begin(), allData.end(), [](const vector<string>& a, const vector<string>& b) {
        
        return stoi(a[0]) < stoi(b[0]);
    });
    
    
    displayTable(headers, allData);
}


int getNextId(const vector<PetShop>& produk, const vector<Aksesoris>& aksesoris, const vector<Baju>& baju) {
    int maxId = 0;
    for (const auto& p : produk) if (p.getId() > maxId) maxId = p.getId();
    for (const auto& a : aksesoris) if (a.getId() > maxId) maxId = a.getId();
    for (const auto& b : baju) if (b.getId() > maxId) maxId = b.getId();
    return maxId + 1;
}


void addNewProduct(vector<PetShop>& produk, vector<Aksesoris>& aksesoris, vector<Baju>& baju) {
    int choice;
    cout << "\nJenis produk yang ingin ditambahkan:" << endl;
    cout << "1. Produk PetShop" << endl;
    cout << "2. Aksesoris" << endl;
    cout << "3. Baju" << endl;
    cout << "Pilihan: ";
    cin >> choice;

    if (cin.fail() || choice < 1 || choice > 3) {
        cout << "Input tidak valid." << endl;
        cin.clear();
        cin.ignore();
        return;
    }

    int id = getNextId(produk, aksesoris, baju);
    string nama;
    double harga;
    int stok;

    cout << "\nMasukkan data produk:" << endl;
    cin.ignore();
    cout << "Nama produk: ";
    getline(cin, nama);

    cout << "Harga produk: Rp";
    cin >> harga;
    if (cin.fail()) {
        cout << "Input harga tidak valid." << endl;
        cin.clear();
        cin.ignore();
        return;
    }

    cout << "Stok produk: ";
    cin >> stok;
    if (cin.fail()) {
        cout << "Input stok tidak valid." << endl;
        cin.clear();
        cin.ignore();
        return;
    }

    if (choice == 1) {
        produk.push_back(PetShop(id, nama, harga, stok));
        cout << "\nProduk PetShop berhasil ditambahkan!" << endl;
    } else if (choice == 2) {
        string jenis, bahan, warna;
        cin.ignore();
        cout << "Jenis aksesoris: ";
        getline(cin, jenis);
        cout << "Bahan: ";
        getline(cin, bahan);
        cout << "Warna: ";
        getline(cin, warna);

        aksesoris.push_back(Aksesoris(id, nama, harga, stok, jenis, bahan, warna));
        cout << "\nAksesoris berhasil ditambahkan!" << endl;
    } else if (choice == 3) {
        string jenis, bahan, warna, untuk, size, merk;
        cin.ignore();
        cout << "Jenis pakaian: ";
        getline(cin, jenis);
        cout << "Bahan: ";
        getline(cin, bahan);
        cout << "Warna: ";
        getline(cin, warna);
        cout << "Untuk (hewan): ";
        getline(cin, untuk);
        cout << "Ukuran: ";
        getline(cin, size);
        cout << "Merk: ";
        getline(cin, merk);

        baju.push_back(Baju(id, nama, harga, stok, jenis, bahan, warna, untuk, size, merk));
        cout << "\nBaju berhasil ditambahkan!" << endl;
    }
}

int main() {
    vector<PetShop> produk = {
        PetShop(1, "Dog Food Premium", 85000, 25),
        PetShop(2, "Cat Litter Box", 120000, 10)
    };

    vector<Aksesoris> aksesoris = {
        Aksesoris(3, "Cat Collar", 35000, 30, "Collar", "Leather", "Black"),
        Aksesoris(4, "Dog Leash", 65000, 15, "Leash", "Nylon", "Red")
    };

    vector<Baju> baju = {
        Baju(5, "Dog Raincoat", 150000, 8, "Coat", "Waterproof", "Yellow", "Anjing", "M", "PawStyle")
    };

    int choice;
    do {
        cout << "\n==== SISTEM MANAJEMEN PETSHOP ====" << endl;
        cout << "1. Tampilkan Semua Produk" << endl;
        cout << "2. Tambah Produk Baru" << endl;
        cout << "0. Keluar" << endl;
        cout << "Pilihan: ";
        cin >> choice;

        if (cin.fail()) {
            cout << "Input tidak valid. Silakan coba lagi." << endl;
            cin.clear();
            cin.ignore();
            continue;
        }

        switch (choice) {
            case 1:
                displayAllProducts(produk, aksesoris, baju);
                break;
            case 2:
                addNewProduct(produk, aksesoris, baju);
                break;
            case 0:
                cout << "Terima kasih telah menggunakan sistem manajemen PetShop." << endl;
                break;
            default:
                cout << "Pilihan tidak valid. Silakan coba lagi." << endl;
                break;
        }
    } while (choice != 0);

    return 0;
}