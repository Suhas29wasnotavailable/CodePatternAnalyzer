class Solution:
 def climbStairs(self,n):
     if n==1:
      return 1
     if n==2:
         return 2
     a=1
     b=2
     i=3
     while i<=n:
      tmp=a+b
      a=b
      b=tmp
      i=i+1
     return b
