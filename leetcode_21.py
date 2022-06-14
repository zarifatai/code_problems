from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def compare(list1: Optional[ListNode], list2: Optional[ListNode]):
            if list1 is None and list2 is not None:
                min_val = list2.val
                list2 = list2.next
                return ListNode(val=min_val, next=compare(list1, list2))
            if list1 is not None and list2 is None:
                min_val = list1.val
                list1 = list1.next
                return ListNode(val=min_val, next=compare(list1, list2))
            if list1 is None and list2 is None:
                return None
            if list1.val < list2.val:
                min_val = list1.val
                list1 = list1.next
            else:
                min_val = list2.val
                list2 = list2.next
            return ListNode(val=min_val, next=compare(list1, list2))

        return compare(list1, list2)

    def merge_two_lists_2(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
