# EXERCISE
# Program an interative binary search that solves for the 3 sets defined here.
arr1 = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
arr2 = [2, 3, 4, 10, 40]
arr3 = [1, 2, 3, 4, 5]


def iterative_binary_search(arr, x) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


assert (r := iterative_binary_search(arr1, 23)) == 5, f"Expected 5, got: {r}"
assert (r := iterative_binary_search(arr2, 10)) == 3, f"Expected 3, got: {r}"
assert (r := iterative_binary_search(arr3, 6)) == -1, f"Expected -1, got: {r}"

# BIG O ANALYSIS
# Time Complexity
#
# - Best Case:
#   In the best case X is right in the middle of the list thus giving us O(1).
#
# - Worst Case:
#   The worst cases seems to happen when X is at the beginning or the end of the
#   list since we always start from the middle. But even in this case we have a
#   time complexity of O(log n)
#
# Space Complexity
# O(3)? Because of the low, high and mid variables.

# REFERENCES
# https://www.geeksforgeeks.org/dsa/binary-search/
