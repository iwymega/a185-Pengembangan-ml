def insertion_sort(numbers: list) -> list:
    sorted_numbers = numbers.copy()
    n = len(sorted_numbers)

    for i in range(1, n):
        key = sorted_numbers[i]
        j = i - 1

        while j >= 0 and key < sorted_numbers[j]:
            sorted_numbers[j + 1] = sorted_numbers[j]
            j -= 1

        sorted_numbers[j + 1] = key

    return sorted_numbers


# main program
numbers = [1, 3, 2, 5, 1, 6, 1, 3, 2, 1]

sorted_data_insertion_sort = insertion_sort(numbers)
print("Data sebelum diurutkan:", numbers)
print("Data setelah diurutkan:", sorted_data_insertion_sort)

"""
Output:
Data sebelum diurutkan: [1, 3, 2, 5, 1, 6, 1, 3, 2, 1]
Data setelah diurutkan: [1, 1, 1, 1, 2, 2, 3, 3, 5, 6]
"""
