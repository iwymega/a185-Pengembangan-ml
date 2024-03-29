"""
TODO:
 1. Buatlah perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel permission.
     1.1. Beri informasi bahwa masukan hanya boleh mengizinkan nilai 1 untuk True atau 0 untuk False.
 2. Buatlah perintah untuk meminta masukan pengguna yang bertipe data string dan simpan pada variabel city.
 3. Buatlah prosedur bernama checkPermission yang memiliki parameter permission dan city.
     3.1. Gunakan pengondisian untuk memeriksa permission.
          3.1.1. Apabila bernilai False, cetak teks "Anda tidak bisa membangun rumah di kota {city} karena berkas belum lengkap."
          3.1.2. Apabila bernilai True, cetak teks "Anda dapat membangun rumah di kota {city}."
     3.2. Jalankan prosedur untuk memeriksa berkas
"""

# Tulis kode Anda di bawah ini
# Masukan nilai izin pembangunan
permission: int = int(
    input("Masukkan izin pembangunan (1 untuk True, 0 untuk False): ")
)

# Masukan nilai kota
city: str = input("Masukkan kota: ")


# Prosedur untuk memeriksa izin pembangunan
def checkPermission(permission: int, city: str):
    # Periksa nilai permission
    if permission == 1:
        print(f"Anda dapat membangun rumah di kota {city}.")
    else:
        print(
            f"Anda tidak bisa membangun rumah di kota {city} karena berkas belum lengkap."
        )


# Menjalankan prosedur checkPermission
checkPermission(permission, city)
