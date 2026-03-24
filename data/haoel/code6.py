def update_current(current, value):
    return max(value, current + value)

def update_maximum(maximum, current):
    return max(maximum, current)

def kadane_step(state, value):
    current, maximum = state
    current = update_current(current, value)
    maximum = update_maximum(maximum, current)
    return current, maximum

def max_subarray(nums):
    current = maximum = nums[0]
    for value in nums[1:]:
        current, maximum = kadane_step((current, maximum), value)
    return maximum
