# EXERCISE
# Given an array, arr[] of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.
arr1 = [1, 2, 3, 4]
arr2 = [10, 8, 30, 4, 5]
arr3 = [10, 8, 30]


def linear_search(arr, x) -> int:
    for i in range(0, len(arr)):
        if arr[i] == x:
            return i
    return -1


assert (r := linear_search(arr1, 3)) == 2, f"Expected 2, got: {r}"
assert (r := linear_search(arr2, 5)) == 4, f"Expected 4, got: {r}"
assert (r := linear_search(arr3, 6)) == -1, f"Expected -1, got: {r}"

# BIG O ANALYSIS
# Time Complexity
#
# - Best Case:
#   X might be present at the first index. The complexity would be O(1)
#
# - Worst Case:
#   X might be present in the last index. Opposite to the end where we started
#   the search. The complexity would be O(n) where n is the size of the list
#
# Space Complexity
# - O(1) as the only variable needed (i) is the one used to iterate through the list

# REFERENCES
# https://www.geeksforgeeks.org/dsa/linear-search/
