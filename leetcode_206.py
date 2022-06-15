class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        return_list = None
        while head:
            return_list = ListNode(val=head.val, next=return_list)
            head = head.next
        return return_list

    def reverse_list_2(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
