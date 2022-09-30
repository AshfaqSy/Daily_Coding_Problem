"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def get_positive_subset(arr):
    i = 0
    j = len(arr) - 1

    while i<j:
        if arr[i] > 0 and arr[j] <= 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        elif arr[i] > 0:
            j -= 1
        else:
            i += 1

    pivot = i if arr[i] > 0 else i + 1
    return arr[pivot:]

def get_missing_number(arr):
    if not arr: return 1

    arr = get_positive_subset(arr)
    arr_len = len(arr)

    if not arr: return 1

    if max(arr) == len(arr):
        return max(arr) + 1

    for num in arr:
        current_num = abs(num)
        if (current_num -1) < arr_len:
            arr[current_num - 1] *= -1

    for i, num in enumerate(arr):
        if num > 0:
            return i + 1


assert get_missing_number([3, 4, -1, 1]) == 2
assert get_missing_number([1, 2, 0]) == 3
assert get_missing_number([1, 2, 5]) == 3
assert get_missing_number([1]) == 2
assert get_missing_number([-1, -2]) == 1
assert get_missing_number([]) == 1
