numbers = [10, 5, 2, 8, 11, 34, 1, 45, 12, 0]


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


bubble_sort(numbers)
print(numbers)
