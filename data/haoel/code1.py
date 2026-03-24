def make_lookup(numbers):
    return {value: index for index, value in enumerate(numbers)}

def find_complement(lookup, numbers, target):
    for index, value in enumerate(numbers):
        complement = target - value
        if complement in lookup and lookup[complement] != index:
            return [index, lookup[complement]]
    return []

def two_sum(numbers, target):
    lookup = make_lookup(numbers)
    return find_complement(lookup, numbers, target)
