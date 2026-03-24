class Solution:
    def maxSubArray(self, nums):
        if nums is not None:
            if len(nums) > 0:
                max_sum = nums[0]
                current_sum = nums[0]
                for i in range(1, len(nums)):
                    if nums[i] is not None:
                        if current_sum + nums[i] > nums[i]:
                            current_sum = current_sum + nums[i]
                        else:
                            current_sum = nums[i]
                        if current_sum > max_sum:
                            max_sum = current_sum
                return max_sum
            else:
                return 0
        else:
            return 0
