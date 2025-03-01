import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {
    public static void displayTable(List<String> headers, List<List<String>> data) {
        
        List<Integer> widths = new ArrayList<>();
        for (int i = 0; i < headers.size(); i++) {
            widths.add(headers.get(i).length());
            for (List<String> row : data) {
                if (i < row.size() && row.get(i).length() > widths.get(i)) {
                    widths.set(i, row.get(i).length());
                }
            }
        }

            
    System.out.print("+");
    for (int w : widths) {
        for (int i = 0; i < w + 2; i++) {
            System.out.print("-");
        }
        System.out.print("+");
    }
    System.out.println();

    System.out.print("|");
    for (int i = 0; i < headers.size(); i++) {
        System.out.printf(" %-" + widths.get(i) + "s |", headers.get(i));
    }
    System.out.println();

    
    System.out.print("+");
    for (int w : widths) {
        for (int i = 0; i < w + 2; i++) {
            System.out.print("-");
        }
        System.out.print("+");
    }
    System.out.println();

        
        for (List<String> row : data) {
            System.out.print("|");
            for (int i = 0; i < headers.size(); i++) {
                String cell = i < row.size() ? row.get(i) : "-";
                System.out.printf(" %-" + widths.get(i) + "s |", cell);
            }
            System.out.println();
        }

        
        System.out.print("+");
        for (int w : widths) {
            for (int i = 0; i < w + 2; i++) {
                System.out.print("-");
            }
            System.out.print("+");
        }
        System.out.println();
    }

    public static void displayAllProducts(List<PetShop> produk, List<Aksesoris> aksesoris, List<Baju> baju) {
    System.out.println("\n=== SEMUA PRODUK PETSHOP ===");
    
    List<String> headers = Arrays.asList(
        "ID", "NAMA PRODUK", "HARGA", "STOK", "KATEGORI", 
        "JENIS", "BAHAN", "WARNA", "UNTUK", "SIZE", "MERK"
    );
    
    List<List<String>> allData = new ArrayList<>();
    
    // Mengumpulkan data dari produk
    for (PetShop p : produk) {
        List<String> row = new ArrayList<>(p.getData());
        row.add(4, "PetShop");
        while (row.size() < headers.size()) {
            row.add("-");
        }
        allData.add(row);
    }
    
    // Mengumpulkan data dari aksesoris
    for (Aksesoris a : aksesoris) {
        List<String> row = new ArrayList<>(a.getData());
        row.add(4, "Aksesoris");
        while (row.size() < headers.size()) {
            row.add("-");
        }
        allData.add(row);
    }
    
    // Mengumpulkan data dari baju
    for (Baju b : baju) {
        List<String> row = new ArrayList<>(b.getData());
        row.add(4, "Baju");
        while (row.size() < headers.size()) {
            row.add("-");
        }
        allData.add(row);
    }
    
    // Mengurutkan data berdasarkan ID menggunakan Stream
    allData = allData.stream()
        .sorted((row1, row2) -> Integer.compare(
            Integer.parseInt(row1.get(0)), 
            Integer.parseInt(row2.get(0))
        ))
        .collect(Collectors.toList());
    
    // Menampilkan tabel
    displayTable(headers, allData);
}

    public static int getNextId(List<PetShop> produk, List<Aksesoris> aksesoris, List<Baju> baju) {
        int maxId = 0;
        for (PetShop p : produk) if (p.getId() > maxId) maxId = p.getId();
        for (Aksesoris a : aksesoris) if (a.getId() > maxId) maxId = a.getId();
        for (Baju b : baju) if (b.getId() > maxId) maxId = b.getId();
        return maxId + 1;
    }

    public static void addNewProduct(List<PetShop> produk, List<Aksesoris> aksesoris, List<Baju> baju) {
        Scanner scanner = new Scanner(System.in);
        int choice;
        System.out.println("\nJenis produk yang ingin ditambahkan:");
        System.out.println("1. Produk PetShop");
        System.out.println("2. Aksesoris");
        System.out.println("3. Baju");
        System.out.print("Pilihan: ");
        choice = scanner.nextInt();

        if (choice < 1 || choice > 3) {
            System.out.println("Input tidak valid.");
            return;
        }

        int id = getNextId(produk, aksesoris, baju);
        scanner.nextLine(); 
        System.out.println("\nMasukkan data produk:");
        System.out.print("Nama produk: ");
        String nama = scanner.nextLine();

        System.out.print("Harga produk: Rp");
        double harga = scanner.nextDouble();

        System.out.print("Stok produk: ");
        int stok = scanner.nextInt();

        if (choice == 1) {
            produk.add(new PetShop(id, nama, harga, stok));
            System.out.println("\nProduk PetShop berhasil ditambahkan!");
        } else if (choice == 2) {
            scanner.nextLine(); 
            System.out.print("Jenis aksesoris: ");
            String jenis = scanner.nextLine();
            System.out.print("Bahan: ");
            String bahan = scanner.nextLine();
            System.out.print("Warna: ");
            String warna = scanner.nextLine();

            aksesoris.add(new Aksesoris(id, nama, harga, stok, jenis, bahan, warna));
            System.out.println("\nAksesoris berhasil ditambahkan!");
        } else if (choice == 3) {
            scanner.nextLine(); 
            System.out.print("Jenis pakaian: ");
            String jenis = scanner.nextLine();
            System.out.print("Bahan: ");
            String bahan = scanner.nextLine();
            System.out.print("Warna: ");
            String warna = scanner.nextLine();
            System.out.print("Untuk (hewan): ");
            String untuk = scanner.nextLine();
            System.out.print("Ukuran: ");
            String size = scanner.nextLine();
            System.out.print("Merk: ");
            String merk = scanner.nextLine();

            baju.add(new Baju(id, nama, harga, stok, jenis, bahan, warna, untuk, size, merk));
            System.out.println("\nBaju berhasil ditambahkan!");
        }
    }

    public static void main(String[] args) {
        List<PetShop> produk = new ArrayList<>();
        produk.add(new PetShop(1, "Dog Food Premium", 85000, 25));
        produk.add(new PetShop(2, "Cat Litter Box", 120000, 10));

        List<Aksesoris> aksesoris = new ArrayList<>();
        aksesoris.add(new Aksesoris(3, "Cat Collar", 35000, 30, "Collar", "Leather", "Black"));
        aksesoris.add(new Aksesoris(4, "Dog Leash", 65000, 15, "Leash", "Nylon", "Red"));

        List<Baju> baju = new ArrayList<>();
        baju.add(new Baju(5, "Dog Raincoat", 150000, 8, "Coat", "Waterproof", "Yellow", "Anjing", "M", "PawStyle"));

        Scanner scanner = new Scanner(System.in);
        int choice;
        do {
            System.out.println("\n==== SISTEM MANAJEMEN PETSHOP ====");
            System.out.println("1. Tampilkan Semua Produk");
            System.out.println("2. Tambah Produk Baru");
            System.out.println("0. Keluar");
            System.out.print("Pilihan: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    displayAllProducts(produk, aksesoris, baju);
                    break;
                case 2:
                    addNewProduct(produk, aksesoris, baju);
                    break;
                case 0:
                    System.out.println("Terima kasih telah menggunakan sistem manajemen PetShop.");
                    break;
                default:
                    System.out.println("Pilihan tidak valid. Silakan coba lagi.");
                    break;
            }
        } while (choice != 0);

        scanner.close();
    }
}