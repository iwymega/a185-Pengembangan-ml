numbers = [23, 99, 55, 49, 89, 72, 9, 13, 42, 62]
number_what_we_looking_for = 42

numbers = sorted(numbers)

low = 0
high = len(numbers) - 1

found = False
mid = 0

while low <= high and not found:
    mid = (low + high) // 2
    mid_value = numbers[mid]

    if mid_value == number_what_we_looking_for:
        found = True
    elif mid_value < number_what_we_looking_for:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print(f"Angka {number_what_we_looking_for} ditemukan pada indeks ke-{mid}.")
else:
    print("Angka tidak ditemukan dalam kumpulan data.")

# Output: Angka 42 ditemukan pada indeks ke-3.
