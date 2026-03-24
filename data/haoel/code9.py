def is_base(n):
    return n <= 2

def base_result(n):
    return n

def step_up(a, b):
    return b, a + b

def compute_steps(n):
    a, b = 1, 2
    for _ in range(n - 2):
        a, b = step_up(a, b)
    return b

def climb_stairs(n):
    if is_base(n):
        return base_result(n)
    return compute_steps(n)
