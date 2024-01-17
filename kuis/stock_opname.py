"""
TODO:
 1. Buatlah variabel chocolateBarStock bertipe data integer yang bernilai 50.
 2. Tambahkan perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel chocolateBarCount.
 3. Gunakan ekspresi yang tepat untuk menghitung total stok camilan dan simpan pada newChocolateBarStock bertipe data integer.
 4. Tampilkan hasil stok baru pada console dengan teks "Stok saat ini adalah {newChocolateBarStock} buah."
"""

# Tulis kode Anda di bawah ini
# 1. Buatlah variabel chocolateBarStock bertipe data integer yang bernilai 50.
chocolateBarStock: int = 50

# 2. Tambahkan perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel chocolateBarCount.
chocolateBarCount: int = int(
    input("Masukkan jumlah chocolate bar yang ingin dibeli oleh Bima: ")
)

# 3. Gunakan ekspresi yang tepat untuk menghitung total stok camilan dan simpan pada newChocolateBarStock bertipe data integer.
newChocolateBarStock: int = chocolateBarStock - chocolateBarCount

# 4. Tampilkan hasil stok baru pada console dengan teks "Stok saat ini adalah {newChocolateBarStock} buah."
print(f"Stok saat ini adalah {newChocolateBarStock} buah.")
