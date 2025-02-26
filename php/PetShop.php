<?php
class PetShop {
    protected $id;
    protected $nama_produk;
    protected $harga_produk;
    protected $stok_produk;
    protected $foto_produk;

    public function __construct($id, $nama, $harga, $stok, $foto = "") {
        $this->id = $id;
        $this->nama_produk = $nama;
        $this->harga_produk = $harga;
        $this->stok_produk = $stok;
        $this->foto_produk = $foto;
    }

    public function get_id() {
        return $this->id;
    }

    public function get_nama() {
        return $this->nama_produk;
    }

    public function get_harga() {
        return $this->harga_produk;
    }

    public function get_stok() {
        return $this->stok_produk;
    }
    
    public function get_foto() {
        return $this->foto_produk;
    }

    
    public function get_column_headers() {
        return ["ID", "NAMA PRODUK", "HARGA", "STOK", "FOTO"];
    }

    public function get_data() {
        $foto_display = empty($this->foto_produk) ? "-" : "<img src='uploads/{$this->foto_produk}' width='50' height='50'>";
        return [
            strval($this->id),
            $this->nama_produk,
            "Rp" . number_format($this->harga_produk, 0, ',', '.'),
            strval($this->stok_produk),
            $foto_display
        ];
    }
}

?>