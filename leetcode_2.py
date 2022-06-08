from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l1_digits = ""
        while l1:
            l1_digits = str(l1.val) + l1_digits
            l1 = l1.next

        l2_digits = ""
        while l2:
            l2_digits = str(l2.val) + l2_digits
            l2 = l2.next

        sum = str(int(l1_digits) + int(l2_digits))[::1]
        print("Sum:", sum)
        head = ListNode(val=int(sum[0]))
        for char in sum[1:]:
            node = ListNode(val=int(char), next=head)
            head = node

        return head
