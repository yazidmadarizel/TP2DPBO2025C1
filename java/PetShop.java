import java.util.ArrayList;
import java.util.List;

class PetShop {
    private int id;
    private String namaProduk;
    private double hargaProduk;
    private int stokProduk;

    public PetShop(int id, String namaProduk, double hargaProduk, int stokProduk) {
        this.id = id;
        this.namaProduk = namaProduk;
        this.hargaProduk = hargaProduk;
        this.stokProduk = stokProduk;
    }

    public int getId() {
        return id;
    }

    public String getNamaProduk() {
        return namaProduk;
    }

    public double getHargaProduk() {
        return hargaProduk;
    }

    public int getStokProduk() {
        return stokProduk;
    }

    public static List<String> getColumnHeaders() {
        List<String> headers = new ArrayList<>();
        headers.add("ID");
        headers.add("NAMA PRODUK");
        headers.add("HARGA");
        headers.add("STOK");
        return headers;
    }

    public List<String> getData() {
        List<String> data = new ArrayList<>();
        data.add(String.valueOf(id));
        data.add(namaProduk);
        data.add("Rp" + String.valueOf(hargaProduk));
        data.add(String.valueOf(stokProduk));
        return data;
    }
}

