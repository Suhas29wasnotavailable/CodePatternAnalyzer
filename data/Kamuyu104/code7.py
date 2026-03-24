class Solution:
    def merge(self,a,b):
        r=[];i=j=0
        while i<len(a) and j<len(b):
            if a[i]<=b[j]:r.append(a[i]);i+=1
            else:r.append(b[j]);j+=1
        return r+a[i:]+b[j:]
