<?php

require('Aksesoris.php'); 

class Baju extends Aksesoris {
    protected $untuk;
    protected $size;
    protected $merk;

    public function __construct($id, $nama, $harga, $stok, $jenis, $bahan, $warna, $untuk, $size, $merk, $foto = "") {
        parent::__construct($id, $nama, $harga, $stok, $jenis, $bahan, $warna, $foto);
        $this->untuk = $untuk;
        $this->size = $size;
        $this->merk = $merk;
    }

    public function get_untuk() {
        return $this->untuk;
    }

    public function get_size() {
        return $this->size;
    }

    public function get_merk() {
        return $this->merk;
    }

    public function get_column_headers() {
        $headers = parent::get_column_headers();
        array_push($headers, "UNTUK", "SIZE", "MERK");
        return $headers;
    }

    public function get_data() {
        $data = parent::get_data();
        array_push($data, $this->untuk, $this->size, $this->merk);
        return $data;
    }
}


?>