def get_mid(left, right):
    return (left + right) // 2

def is_target(nums, mid, target):
    return nums[mid] == target

def go_right(nums, mid, target):
    return nums[mid] < target

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = get_mid(left, right)
        if is_target(nums, mid, target):
            return mid
        elif go_right(nums, mid, target):
            left = mid + 1
        else:
            right = mid - 1
    return -1
