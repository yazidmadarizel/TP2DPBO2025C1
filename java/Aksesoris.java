import java.util.List;

class Aksesoris extends PetShop {
    private String jenis;
    private String bahan;
    private String warna;

    public Aksesoris(int id, String namaProduk, double hargaProduk, int stokProduk, String jenis, String bahan, String warna) {
        super(id, namaProduk, hargaProduk, stokProduk);
        this.jenis = jenis;
        this.bahan = bahan;
        this.warna = warna;
    }

    public String getJenis() {
        return jenis;
    }

    public String getBahan() {
        return bahan;
    }

    public String getWarna() {
        return warna;
    }

    public static List<String> getColumnHeaders() {
        List<String> headers = PetShop.getColumnHeaders();
        headers.add("JENIS");
        headers.add("BAHAN");
        headers.add("WARNA");
        return headers;
    }

    public List<String> getData() {
        List<String> data = super.getData();
        data.add(jenis);
        data.add(bahan);
        data.add(warna);
        return data;
    }
}

