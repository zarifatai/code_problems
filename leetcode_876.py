from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        length = 0
        while node:
            length += 1
            node = node.next

        counter = 0
        node = head
        while counter < length // 2:
            counter += 1
            node = node.next
        return node
