def base_case(n):
    return n <= 1

def next_fib(a, b):
    return b, a + b

def iterate_fib(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = next_fib(a, b)
    return b

def fib(n):
    if base_case(n):
        return n
    return iterate_fib(n)
