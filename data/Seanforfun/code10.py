class Solution:
    def isPalindrome(self,s):
     clean=[]
     for c in s:
         if c.isalnum():
          clean.append(c.lower())
     l=0
     r=len(clean)-1
     while l<r:
         if clean[l]!=clean[r]:
          return False
         l=l+1
         r=r-1
     return True
