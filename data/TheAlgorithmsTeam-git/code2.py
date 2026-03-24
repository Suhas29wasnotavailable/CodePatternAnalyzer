class ListNode:
    def __init__(self, node_value: int = 0, next_node=None):
        self.node_value = node_value
        self.next_node = next_node


class Solution:
    def reverse_linked_list(self, head_node: ListNode) -> ListNode:
        """
        Reverse a singly linked list iteratively.
        Returns the new head of the reversed list.
        """
        previous_node = None
        current_node = head_node

        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node

        return previous_node
