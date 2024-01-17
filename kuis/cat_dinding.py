"""
TODO:
 1. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel panjangRuang.
 2. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel lebarRuang.
 3. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel tinggiRuang.
 4. Buatlah fungsi bernama hitungCat yang memiliki parameter panjangRuang, lebarRuang, dan tinggiRuang.
    4.1. Hitung keliling ruangan dengan rumus keliling persegi panjang dan simpan pada variabel kelilingRuang.
    4.2. Hitung jumlah liter cat yang akan dipakai dengan rumus di atas.
    4.3. Fungsi ini mengembalikan nilai float yang menyatakan jumlah liter cat berdasarkan ketiga nilai tersebut.
    4.4. Simpan hasil fungsi pada variabel jumlahLiter.
 5. Cetak nilai jumlahLiter pada teks "Jumlah cat yang Anda perlukan adalah {jumlahLiter} liter."
"""

# Tulis kode Anda di bawah ini
# Masukan nilai panjang, lebar, dan tinggi ruangan
panjangRuang: float = float(input("Masukkan panjang ruangan (dalam meter): "))
lebarRuang: float = float(input("Masukkan lebar ruangan (dalam meter): "))
tinggiRuang: float = float(input("Masukkan tinggi ruangan (dalam meter): "))


# Fungsi untuk menghitung jumlah liter cat
def hitungCat(panjangRuang: float, lebarRuang: float, tinggiRuang: float) -> float:
    # Hitung keliling ruangan
    kelilingRuang = 2 * (panjangRuang + lebarRuang)

    # Hitung jumlah liter cat yang akan dipakai
    jumlahLiter = kelilingRuang * tinggiRuang / 12

    return jumlahLiter


# Menghitung jumlah liter cat yang dibutuhkan
jumlahLiter: float = hitungCat(panjangRuang, lebarRuang, tinggiRuang)

# Mencetak hasil
print(f"Jumlah cat yang Anda perlukan adalah {jumlahLiter} liter.")
