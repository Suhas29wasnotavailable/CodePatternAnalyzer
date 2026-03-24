def get_next(node):
    return node.next if node else None

def set_next(node, new_next):
    node.next = new_next
    return node

def reverse_step(prev, curr):
    nxt = get_next(curr)
    set_next(curr, prev)
    return curr, nxt

def reverse_linked_list(head):
    prev, curr = None, head
    while curr:
        prev, curr = reverse_step(prev, curr)
    return prev
