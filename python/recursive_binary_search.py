# EXERCISE
# Program a recursive binary search that solves for the 3 sets defined here.
arr1 = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
arr2 = [2, 3, 4, 10, 40]
arr3 = [1, 2, 3, 4, 5]


def recursive_binary_search(arr: list, x: int, high: int, low: int = 0) -> int:
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if arr[mid] == x:
        return mid
    if x > arr[mid]:
        return recursive_binary_search(arr, x, high, mid + 1)
    else:
        return recursive_binary_search(arr, x, mid - 1, low)


assert (
    r := recursive_binary_search(arr1, 23, len(arr1) - 1)
) == 5, f"Expected 5, got: {r}"
assert (
    r := recursive_binary_search(arr2, 10, len(arr2) - 1)
) == 3, f"Expected 3, got: {r}"
assert (
    r := recursive_binary_search(arr3, 6, len(arr3) - 1)
) == -1, f"Expected -1, got: {r}"

# BIG O ANALYSIS
#
# Time Complexity:
# Best Case: O(1)
# The target element `x` is found exactly at the middle index on the very first
# attempt.
#
# Worst Case: O(log n)
# The target element is at the extreme ends of the array or not present at all.
# The algorithm must continuously divide the search space in half until `low > high`.
#
# Space Complexity: O(log n)
# While the array itself takes O(n) space, the algorithm only passes references.
# However, each recursive step adds a new frame to the function call stack. In
# the worst-case scenario, the stack reaches a depth of log(n).

# REFERENCES
# https://www.geeksforgeeks.org/dsa/binary-search/
