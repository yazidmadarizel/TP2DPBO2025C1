<?php

require('PetShop.php'); 

class Aksesoris extends PetShop {
    protected $jenis;
    protected $bahan;
    protected $warna;

    public function __construct($id, $nama, $harga, $stok, $jenis, $bahan, $warna, $foto = "") {
        parent::__construct($id, $nama, $harga, $stok, $foto);
        $this->jenis = $jenis;
        $this->bahan = $bahan;
        $this->warna = $warna;
    }

    public function get_jenis() {
        return $this->jenis;
    }

    public function get_bahan() {
        return $this->bahan;
    }

    public function get_warna() {
        return $this->warna;
    }

    public function get_column_headers() {
        $headers = parent::get_column_headers();
        array_push($headers, "JENIS", "BAHAN", "WARNA");
        return $headers;
    }

    public function get_data() {
        $data = parent::get_data();
        array_push($data, $this->jenis, $this->bahan, $this->warna);
        return $data;
    }
}

?>