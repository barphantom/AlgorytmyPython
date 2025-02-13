numbers = [10, 5, 2, 8, 11, 34, 1, 45, 12, 0, 100]
nums1 = [1, 2, 3, 7, 7]
nums2 = [7, 8, 9, 9]


def pivot(array, pivot_index, end_index):
    swap = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if array[i] < array[pivot_index]:
            swap += 1
            array[i], array[swap] = array[swap], array[i]
    array[pivot_index], array[swap] = array[swap], array[pivot_index]
    return swap


def quick_sort_helper(array, left, right):
    if left < right:
        pivot_index = pivot(array, left, right)
        quick_sort_helper(array, left, pivot_index - 1)
        quick_sort_helper(array, pivot_index + 1, right)
    return array


def quick_sort(array):
    return quick_sort_helper(array, 0, len(array) - 1)


# print(pivot(numbers, 0, len(numbers) - 1))
# print(numbers)
new_list = quick_sort(numbers)
print(new_list)
