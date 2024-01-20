numbers = [23, 99, 55, 49, 89, 72, 9, 13, 42, 62]
number_what_we_looking_for = 42

found = False
i = 0

while i < len(numbers) and not found:
    if numbers[i] == number_what_we_looking_for:
        found = True
    else:
        i = i + 1

if found:
    print(f"Angka {number_what_we_looking_for} ditemukan pada indeks ke-{i}.")
else:
    print("Angka tidak ditemukan dalam kumpulan data.")

# Output: Angka 42 ditemukan pada indeks ke-8.
