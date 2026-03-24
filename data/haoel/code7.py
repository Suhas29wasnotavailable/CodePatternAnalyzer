def take_smaller(a, b, i, j):
    if a[i] <= b[j]:
        return a[i], i + 1, j
    return b[j], i, j + 1

def drain(arr, index):
    return arr[index:]

def merge_arrays(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        val, i, j = take_smaller(a, b, i, j)
        result.append(val)
    return result + drain(a, i) + drain(b, j)
