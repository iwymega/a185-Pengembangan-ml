def sequential_search_without_boolean(arr: list, target: any) -> int:
    i = 0
    while i < len(numbers):
        if numbers[i] == number_what_we_looking_for:
            return i
        i = i + 1
    return -1

numbers = [23,99,55,49,89,72,9,13,42,62]
number_what_we_looking_for = 52

output = sequential_search_without_boolean(numbers, number_what_we_looking_for)
if output != -1:
    print(f"Angka {number_what_we_looking_for} ditemukan pada indeks ke-{output}.")
else:
    print("Angka tidak ditemukan dalam kumpulan data.")

# Output: Angka tidak ditemukan dalam kumpulan data.