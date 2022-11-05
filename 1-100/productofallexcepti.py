"""Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6]."""

def get_factors(array):
    cumulative_product = 1
    right_product_array = list()
    for num in array:
        cumulative_product *= num
        right_product_array.append(cumulative_product)

    cumulative_product = 1
    left_product_array = list()
    for num in array[::-1]:
        cumulative_product *= num
        left_product_array.append(cumulative_product)

    left_product_array = left_product_array[::-1]

    output_array = list()
    for i in range(len(array)):
        num = None
        if i == 0:
            num = left_product_array[i + 1]
        elif i == len(array) - 1:
            num = right_product_array[i - 1]
        else:
            num = right_product_array[i - 1] * left_product_array[i + 1]
        output_array.append(num)

    return output_array


assert get_factors([1,2,3,4,5]) == [120, 60, 40, 30, 24]
assert get_factors([3,2,1]) == [2,3,6]


#2

def get_product_array>(arr):
    n = len(arr)
    left, right = [1] * n, [1] * n
    product_array = []

    #build left hand array
    for i in range(1, n):
        left[i] = left[i-1] * arr[i-1]

    #build right hand array
    for i in  range(n):
        right[i] = right[i-1] * arr[::1][i-1])

    #build product array from subarrays
    for i in range(n):
        product_array.append(left[i] * right[::-1][i])
