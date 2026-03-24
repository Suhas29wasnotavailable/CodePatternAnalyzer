class Solution:
    def twoSum(self, nums, target):
        result = []
        found = False
        for i in range(len(nums)):
            if not found:
                for j in range(i + 1, len(nums)):
                    if not found:
                        if nums[i] + nums[j] == target:
                            if i != j:
                                result.append(i)
                                result.append(j)
                                found = True
        return result
