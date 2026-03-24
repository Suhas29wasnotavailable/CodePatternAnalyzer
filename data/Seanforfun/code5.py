class Solution:
 def fib(self,n):
     if n==0:
      return 0
     if n==1:
         return 1
     a=0
     b=1
     i=2
     while i<=n:
      c=a+b
      a=b
      b=c
      i=i+1
     return b
