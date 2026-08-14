# 1) Write a Python program to calculate the sum of a list of numbers using recursion.
x = [1, 2, 3]

# Original solution:
def sum_list_rec(x: list, i: int = 1) -> int:
    if len(x) == 0: return 0
    if i > len(x)-1: return x[0]
    return x[i] + sum_list_rec(x, i+1)

# Suggested solution:
def _sum_list_rec(x: list, i: int = 0) -> int:
    if i >= len(x): return 0
    return x[i] + _sum_list_rec(x, i+1)

# 2) Write a Python program to sum nested lists using recursion.
y = [1, 2, [3, 4, [5, 6]]]

def sum_nested_list_rec(y: list, i: int = 0) -> int:
    if i >= len(y): return 0
    if type(y[i]) == list:
        return sum_nested_list_rec(y, i+1) + sum_nested_list_rec(y[i])
    else:
        return y[i] + sum_nested_list_rec(y, i+1)

# 3) Write a Python program to get the sum of a non-negative integer using recursion.
def sum_digits_rec(z: int, i: int = 0) -> int:
    if i >= len(str(z)):
        return 0
    else:
        return int(str(z)[i]) + sum_digits_rec(z, i+1)

# Solution without string conversion:
def noconv_sum_digit_rec(z: int) -> int:
    if z < 10: return z
    return z % 10 + noconv_sum_digit_rec(z // 10)

# 4) Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0) using recursion .
def sum_seq_rec(n: int) -> int:
    if n <= 0:
        return 0
    return n + sum_seq_rec(n-2)

# 5) Write a Python program to calculate the sum of harmonic series upto n terms.
def harm_series_sum_rec(n: int, x: int = 1) -> float:
    if x > n: return 0
    return 1 / x + harm_series_sum_rec(n, (x+1))

# Solution with single parameter:
def _harm_series_sum_rec(n: int) -> float:
    if n < 1: return 0
    return 1 / n + _harm_series_sum_rec(n-1)

# 6) Write a Python program to calculate the geometric sum up to n terms
def geo_series_sum_rec(a: int, b: int) -> float:
    if b < 1: return 0
    return + geo_series_sum_rec(a, )

# Reference:
# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php
