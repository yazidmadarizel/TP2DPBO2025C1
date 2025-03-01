import java.util.List;

class Baju extends Aksesoris {
    private String untuk;
    private String size;
    private String merk;

    public Baju(int id, String namaProduk, double hargaProduk, int stokProduk, String jenis, String bahan, String warna, String untuk, String size, String merk) {
        super(id, namaProduk, hargaProduk, stokProduk, jenis, bahan, warna);
        this.untuk = untuk;
        this.size = size;
        this.merk = merk;
    }

    public String getUntuk() {
        return untuk;
    }

    public String getSize() {
        return size;
    }

    public String getMerk() {
        return merk;
    }

    public static List<String> getColumnHeaders() {
        List<String> headers = Aksesoris.getColumnHeaders();
        headers.add("UNTUK");
        headers.add("SIZE");
        headers.add("MERK");
        return headers;
    }

    public List<String> getData() {
        List<String> data = super.getData();
        data.add(untuk);
        data.add(size);
        data.add(merk);
        return data;
    }
}

