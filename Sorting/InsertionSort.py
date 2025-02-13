numbers = [10, 5, 2, 8, 11, 34, 1, 45, 12, 0]


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1


insertion_sort(numbers)
print(numbers)
