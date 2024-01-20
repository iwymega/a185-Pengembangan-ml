def selection_sort(numbers: list) -> list:
    sorted_numbers = numbers.copy()
    n = len(sorted_numbers)
    for i in range(n):
        # Anggap elemen pertama dari sisa data yang belum diurutkan adalah elemen terkecil
        min_index = i

        # Mencari elemen terkecil dari sisa data yang belum diurutkan
        for j in range(i + 1, n):
            if sorted_numbers[j] < sorted_numbers[min_index]:
                min_index = j

        # Menukar elemen terkecil dengan elemen pertama dari data yang belum diurutkan
        sorted_numbers[i], sorted_numbers[min_index] = (
            sorted_numbers[min_index],
            sorted_numbers[i],
        )

    return sorted_numbers


# main program
numbers = [1, 3, 2, 5, 1, 6, 1, 3, 2, 1]

sorted_data_selection_sort = selection_sort(numbers)
print("Data sebelum diurutkan:", numbers)
print("Data setelah diurutkan:", sorted_data_selection_sort)

"""
Output:
Data sebelum diurutkan: [1, 3, 2, 5, 1, 6, 1, 3, 2, 1]
Data setelah diurutkan: [1, 1, 1, 1, 2, 2, 3, 3, 5, 6]
"""
