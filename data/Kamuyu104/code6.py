class Solution:
    def maxSubArray(self,a):
        mx=cur=a[0]
        for x in a[1:]:
            cur=max(x,cur+x);mx=max(mx,cur)
        return mx
