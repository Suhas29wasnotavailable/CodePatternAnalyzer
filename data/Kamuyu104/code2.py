class Solution:
    def reverseList(self,h):
        p=None
        while h:
            n=h.next;h.next=p;p=h;h=n
        return p
