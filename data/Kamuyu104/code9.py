class Solution:
    def climbStairs(self,n):
        a,b=1,2
        for _ in range(2,n):a,b=b,a+b
        return b if n>1 else 1
