class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    output, current = None, head

    while current:
        remaining = current.next
        current.next = output
        output = current
        current = remaining
    return output
