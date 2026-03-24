class Solution:
    def reverseList(self, head):
        if head is not None:
            if head.next is not None:
                prev = None
                curr = head
                while curr is not None:
                    if curr.next is not None:
                        nxt = curr.next
                        curr.next = prev
                        prev = curr
                        curr = nxt
                    else:
                        curr.next = prev
                        prev = curr
                        curr = None
                return prev
            else:
                return head
        else:
            return None
