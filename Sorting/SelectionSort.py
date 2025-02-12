numbers = [10, 5, 2, 8, 11, 34, 1, 45, 12, 0]


def selection_sort(array):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        if i != min_index:
            array[i], array[min_index] = array[min_index], array[i]


selection_sort(numbers)
print(numbers)
