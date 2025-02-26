<?php
require('Baju.php'); 

function display_table($headers, $data) {
    echo "<table border='1' cellpadding='5' cellspacing='0'>";
    echo "<tr>";
    foreach ($headers as $header) {
        echo "<th>$header</th>";
    }
    echo "</tr>";

    foreach ($data as $row) {
        echo "<tr>";
        foreach ($headers as $index => $header) {
            if (isset($row[$index])) {
                echo "<td>{$row[$index]}</td>";
            } else {
                echo "<td>-</td>";
            }
        }
        echo "</tr>";
    }
    echo "</table>";
}

function display_all_products($produk, $aksesoris, $baju) {
    
    
    $headers = [
        "ID", "NAMA PRODUK", "HARGA", "STOK", "FOTO", "KATEGORI", 
        "JENIS", "BAHAN", "WARNA", "UNTUK", "SIZE", "MERK"
    ];
    
    
    $all_data = [];
    
    
    foreach ($produk as $p) {
        $row = $p->get_data();
        array_splice($row, 5, 0, ["PetShop"]);
        while (count($row) < count($headers)) {
            $row[] = "-";
        }
        $all_data[] = $row;
    }
    
    
    foreach ($aksesoris as $a) {
        $row = $a->get_data();
        array_splice($row, 5, 0, ["Aksesoris"]);
        while (count($row) < count($headers)) {
            $row[] = "-";
        }
        $all_data[] = $row;
    }
    
    
    foreach ($baju as $b) {
        $row = $b->get_data();
        array_splice($row, 5, 0, ["Baju"]);
        while (count($row) < count($headers)) {
            $row[] = "-";
        }
        $all_data[] = $row;
    }
    
    
    usort($all_data, function($a, $b) {
        return intval($a[0]) <=> intval($b[0]);
    });

    
    display_table($headers, $all_data);
}


function get_next_id($produk, $aksesoris, $baju) {
    $max_id = 0;
    foreach ($produk as $p) {
        if ($p->get_id() > $max_id) {
            $max_id = $p->get_id();
        }
    }
    foreach ($aksesoris as $a) {
        if ($a->get_id() > $max_id) {
            $max_id = $a->get_id();
        }
    }
    foreach ($baju as $b) {
        if ($b->get_id() > $max_id) {
            $max_id = $b->get_id();
        }
    }
    return $max_id + 1;
}

function handle_upload() {
    if (!isset($_FILES['foto_produk']) || $_FILES['foto_produk']['error'] === UPLOAD_ERR_NO_FILE) {
        return "";
    }
    
    $target_dir = "uploads/";
    
    
    if (!file_exists($target_dir)) {
        mkdir($target_dir, 0777, true);
    }
    
    $file_extension = pathinfo($_FILES["foto_produk"]["name"], PATHINFO_EXTENSION);
    $filename = pathinfo($_FILES["foto_produk"]["name"], PATHINFO_FILENAME) . "." . $file_extension;

    $target_file = $target_dir . $filename;
    
    if (move_uploaded_file($_FILES["foto_produk"]["tmp_name"], $target_file)) {
        return $filename;
    } 
}


session_start();

if (!isset($_SESSION['produk'])) {
    $_SESSION['produk'] = [
        new PetShop(1, "Dog Food Premium", 85000, 25, "dog_food.jpeg"),
        new PetShop(2, "Cat Litter Box", 120000, 10, "litter_box.jpeg")
    ];
}

if (!isset($_SESSION['aksesoris'])) {
    $_SESSION['aksesoris'] = [
        new Aksesoris(3, "Cat Collar", 35000, 30, "Collar", "Leather", "Black", "cat_collar.jpeg"),
        new Aksesoris(4, "Dog Leash", 65000, 15, "Leash", "Nylon", "Red", "dog_leash.jpeg")
    ];
}

if (!isset($_SESSION['baju'])) {
    $_SESSION['baju'] = [
        new Baju(5, "Dog Raincoat", 150000, 8, "Coat", "Waterproof", "Yellow", "Anjing", "M", "PawStyle", "raincoat.jpeg")
    ];
}

$produk = &$_SESSION['produk'];
$aksesoris = &$_SESSION['aksesoris'];
$baju = &$_SESSION['baju'];


if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['action'])) {
    if ($_POST['action'] == 'add_product') {
        $id = get_next_id($produk, $aksesoris, $baju);
        $nama = $_POST['nama'] ?? '';
        $harga = floatval($_POST['harga'] ?? 0);
        $stok = intval($_POST['stok'] ?? 0);
        $jenis_produk = $_POST['jenis_produk'] ?? '';
        
        $foto = handle_upload();
        
        if ($jenis_produk == "1") {
            $produk[] = new PetShop($id, $nama, $harga, $stok, $foto);
        } 
        elseif ($jenis_produk == "2") {
            $jenis = $_POST['jenis'] ?? '';
            $bahan = $_POST['bahan'] ?? '';
            $warna = $_POST['warna'] ?? '';
            $aksesoris[] = new Aksesoris($id, $nama, $harga, $stok, $jenis, $bahan, $warna, $foto);
        } 
        elseif ($jenis_produk == "3") {
            $jenis = $_POST['jenis'] ?? '';
            $bahan = $_POST['bahan'] ?? '';
            $warna = $_POST['warna'] ?? '';
            $untuk = $_POST['untuk'] ?? '';
            $size = $_POST['size'] ?? '';
            $merk = $_POST['merk'] ?? '';
            $baju[] = new Baju($id, $nama, $harga, $stok, $jenis, $bahan, $warna, $untuk, $size, $merk, $foto);
        }

        
        header("Location: ?action=view");
        exit;
    }
}


?>

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistem Manajemen PetShop</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1, h2 { color: #333; }
        table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
        th { background-color: #f2f2f2; }
        th, td { padding: 8px; text-align: left; }
        form { max-width: 600px; margin-top: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; }
        input[type="text"], input[type="number"], select { width: 100%; padding: 8px; box-sizing: border-box; }
        button { padding: 10px 15px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
        button:hover { background-color: #45a049; }
        .dynamic-fields { margin-top: 15px; }
    </style>
</head>
<body>
    <h1>SISTEM MANAJEMEN PETSHOP</h1>
    
    <?php
    if (!isset($_GET['action']) || $_GET['action'] == 'view') {
        display_all_products($produk, $aksesoris, $baju);
        echo '<div style="margin-top: 20px;">
            <a href="?action=add"><button>Tambah Produk Baru</button></a>
        </div>';
    } 
    elseif ($_GET['action'] == 'add') {
    ?>
        <h2>Tambah Produk Baru</h2>
        <form method="post" enctype="multipart/form-data">
            <input type="hidden" name="action" value="add_product">
            
            <div class="form-group">
                <label for="jenis_produk">Jenis Produk:</label>
                <select id="jenis_produk" name="jenis_produk" onchange="showFields()">
                    <option value="">-- Pilih Jenis Produk --</option>
                    <option value="1">Produk PetShop</option>
                    <option value="2">Aksesoris</option>
                    <option value="3">Baju</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="nama">Nama Produk:</label>
                <input type="text" id="nama" name="nama" required>
            </div>
            
            <div class="form-group">
                <label for="harga">Harga Produk (Rp):</label>
                <input type="number" id="harga" name="harga" min="0" required>
            </div>
            
            <div class="form-group">
                <label for="stok">Stok Produk:</label>
                <input type="number" id="stok" name="stok" min="0" required>
            </div>
            
            <div class="form-group">
                <label for="foto_produk">Foto Produk:</label>
                <input type="file" id="foto_produk" name="foto_produk">
            </div>
            
            <div id="aksesoris_fields" class="dynamic-fields" style="display: none;">
                <div class="form-group">
                    <label for="jenis">Jenis Aksesoris:</label>
                    <input type="text" id="jenis" name="jenis">
                </div>
                
                <div class="form-group">
                    <label for="bahan">Bahan:</label>
                    <input type="text" id="bahan" name="bahan">
                </div>
                
                <div class="form-group">
                    <label for="warna">Warna:</label>
                    <input type="text" id="warna" name="warna">
                </div>
            </div>
            
            <div id="baju_fields" class="dynamic-fields" style="display: none;">
                <div class="form-group">
                    <label for="untuk">Untuk (Hewan):</label>
                    <input type="text" id="untuk" name="untuk">
                </div>
                
                <div class="form-group">
                    <label for="size">Ukuran:</label>
                    <input type="text" id="size" name="size">
                </div>
                
                <div class="form-group">
                    <label for="merk">Merk:</label>
                    <input type="text" id="merk" name="merk">
                </div>
            </div>
            
            <button type="submit">Simpan</button>
            <a href="?action=view"><button type="button">Batal</button></a>
        </form>
        
        <script>
            function showFields() {
                var jenis = document.getElementById('jenis_produk').value;
                var aksesorisFields = document.getElementById('aksesoris_fields');
                var bajuFields = document.getElementById('baju_fields');
                
                aksesorisFields.style.display = 'none';
                bajuFields.style.display = 'none';
                
                if (jenis === '2' || jenis === '3') {
                    aksesorisFields.style.display = 'block';
                }
                
                if (jenis === '3') {
                    bajuFields.style.display = 'block';
                }
            }
        </script>
    <?php
    }
    ?>
</body>
</html>