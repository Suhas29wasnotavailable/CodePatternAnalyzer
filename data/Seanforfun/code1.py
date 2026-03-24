class Solution:
 def twoSum(self, nums, target):
  d = {}
  for i in range(len(nums)):
      n = nums[i]
      x = target - n
      if x in d:
       return [d[x], i]
      else:
          d[n] = i
  return []
