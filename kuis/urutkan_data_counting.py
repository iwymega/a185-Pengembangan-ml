def counting_sort(numbers: list) -> list:
    max_value = max(numbers)  # Menentukan nilai maksimum dalam data
    min_value = min(numbers)  # Menentukan nilai minimum dalam data
    range_values = max_value - min_value + 1  # Mencari rentang nilai data

    # Membuat list kosong untuk menyimpan frekuensi kemunculan setiap nilai
    count = [0] * range_values

    # Menghitung frekuensi kemunculan setiap nilai dalam data
    for num in numbers:
        count[num - min_value] += 1

    # Mengakumulasi jumlah dalam count list
    for i in range(1, range_values):
        count[i] += count[i - 1]

    # Membuat list kosong baru untuk menyimpan data yang sudah diurutkan
    sorted_numbers = [0] * len(numbers)

    # Mengatur data yang akan diurutkan berdasarkan count list
    for num in numbers:
        index = count[num - min_value] - 1
        sorted_numbers[index] = num
        count[num - min_value] -= 1
    return sorted_numbers


# main program
numbers = [1, 3, 2, 5, 1, 6, 1, 3, 2, 1]

sorted_data_counting_sort = counting_sort(numbers)
print("Data sebelum diurutkan:", numbers)
print("Data setelah diurutkan:", sorted_data_counting_sort)

"""
Output:
Data sebelum diurutkan: [1, 3, 2, 5, 1, 6, 1, 3, 2, 1]
Data setelah diurutkan: [1, 1, 1, 1, 2, 2, 3, 3, 5, 6]
"""
