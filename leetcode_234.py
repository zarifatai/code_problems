from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        if values == values[::-1]:
            return True
        else:
            return False
