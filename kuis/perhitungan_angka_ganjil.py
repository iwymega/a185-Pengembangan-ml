"""
TODO:
 1. Buatlah variabel a bertipe data integer yang bernilai 1 untuk menyimpan nilai suku pertama.
 2. Buatlah variabel b bertipe data integer yang bernilai 2 untuk menyimpan nilai beda antar suku.
 3. Buatlah perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel n sebagai nilai suku yang ingin diketahui.
 4. Lakukan perulangan mulai dari 1 hingga n+1 dengan
    4.1. state i;
    4.2. menghitung suku ke-n berdasarkan state i dan simpan pada variabel Un; dan
    4.3. mencetak setiap variabel Un menggunakan perintah print dan parameter end.
 5. Lakukan pemberhentian mencetak teks dengan perintah print tanpa isi.
"""

# Tulis kode Anda di bawah ini
# Program untuk menampilkan deret aritmetika

# Deklarasi variabel
a: int = 1
b: int = 2
n: int = int(input("Masukkan nilai suku yang ingin diketahui: "))

# Perulangan untuk menampilkan deret aritmetika
for i in range(n):
    Un = a + i * b

    # Mencetak suku ke-n
    print(Un, end=" ")

# Pemberhentian mencetak teks
print()
