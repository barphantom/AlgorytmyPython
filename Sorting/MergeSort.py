numbers = [10, 5, 2, 8, 11, 34, 1, 45, 12, 0, 100]
nums1 = [1, 2, 3, 7, 7]
nums2 = [7, 8, 9, 9]


def merge(list1, list2):
    combined = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


def merge_sort(array):
    if len(array) == 1:
        return array
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    return merge(left, right)


new_list = merge_sort(numbers)
# merged_list = merge(nums2, nums1)
print(new_list)
