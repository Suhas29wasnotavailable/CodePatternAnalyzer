class Solution:
    def maxSubArray(self,nums):
     mx=nums[0]
     cur=nums[0]
     i=1
     while i<len(nums):
         val=nums[i]
         if cur+val>val:
          cur=cur+val
         else:
             cur=val
         if cur>mx:
          mx=cur
         i=i+1
     return mx
