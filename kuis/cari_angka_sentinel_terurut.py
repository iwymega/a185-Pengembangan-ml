numbers = [23, 99, 55, 49, 89, 72, 9, 13, 42, 62]
number_what_we_looking_for = 42

numbers = sorted(numbers)

i = 0

last = numbers.pop()
numbers.append(number_what_we_looking_for)

while numbers[i] != number_what_we_looking_for:
    i = i + 1

numbers[-1] = last

if i < len(numbers) - 1 or numbers[-1] == number_what_we_looking_for:
    print(f"Angka {number_what_we_looking_for} ditemukan pada indeks ke-{i}.")
else:
    print("Angka tidak ditemukan dalam kumpulan data.")

# Output: Angka 42 ditemukan pada indeks ke-3.
