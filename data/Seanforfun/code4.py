class Solution:
    def isValid(self, s):
     stk=[]
     for ch in s:
         if ch=='(' or ch=='[' or ch=='{':
          stk.append(ch)
         else:
             if len(stk)==0:
              return False
             top=stk[len(stk)-1]
             if ch==')' and top=='(':
                 stk.pop()
             elif ch==']' and top=='[':
              stk.pop()
             elif ch=='}' and top=='{':
                 stk.pop()
             else:
              return False
     if len(stk)==0:
         return True
     return False
