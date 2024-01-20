def bubble_sort(numbers: list) -> list:
    sorted_numbers = numbers.copy()
    n = len(sorted_numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                sorted_numbers[j], sorted_numbers[j + 1] = (
                    sorted_numbers[j + 1],
                    sorted_numbers[j],
                )

    return sorted_numbers


# main program
numbers = [1, 3, 2, 5, 1, 6, 1, 3, 2, 1]

sorted_data_bubble_sort = bubble_sort(numbers)
print("Data sebelum diurutkan:", numbers)
print("Data setelah diurutkan:", sorted_data_bubble_sort)

"""
Output:
Data sebelum diurutkan: [1, 3, 2, 5, 1, 6, 1, 3, 2, 1]
Data setelah diurutkan: [1, 1, 1, 1, 2, 2, 3, 3, 5, 6]
"""
