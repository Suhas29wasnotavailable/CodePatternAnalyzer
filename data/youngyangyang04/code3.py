class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid >= 0:
                    if mid < len(nums):
                        return mid
            elif nums[mid] < target:
                if left <= mid:
                    left = mid + 1
                else:
                    return -1
            else:
                if right >= mid:
                    right = mid - 1
                else:
                    return -1
        return -1
