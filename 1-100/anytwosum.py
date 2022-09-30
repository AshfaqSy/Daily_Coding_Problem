"Q: Given a list of numbers, return whether any two sums to k. For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17."

def check_sums(array, k):
    potential_sums = set()
    for num in array:
        if num in potential_sums:
            return True
        potential_sums.add(k - num)
    return False

assert not check_sums([], 8)
assert check_sums([10, 7, 8, 9], 17)
assert not check_sums([12, 4, 7, 1], 17)
