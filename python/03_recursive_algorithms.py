def iterative_multiplication(a: int, b: int) -> int:
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result


def recursive_multiplication(a: int, b: int) -> int:
    if b == 0:
        return 0
    elif b < 0:
        return -recursive_multiplication(a, -b)
    else:
        return a + recursive_multiplication(a, b - 1)


def fact(n: int) -> int:
    """Assumes n is an int > 0"""
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


# Solving ToH puzzle recursively
def print_move(fr: int, to: int) -> None:
    print(f"move from {fr} to {to}")


def towers(n: int, fr: int, to: int, spare: int) -> None:
    """Assumes n is an int > 0"""
    if n == 1:
        print_move(fr, to)
    else:
        towers(n - 1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n - 1, spare, to, fr)


# Solving Fibonnaci's Sequence recursively
def fib(x: int) -> int:
    """Assumes x is an int >= 0"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)
