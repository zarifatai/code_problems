class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node(head):
    length = 1
    temp = head
    while head.next:
        head = head.next
        length += 1
    head = temp
    idx = length // 2

    for i in range(idx):
        head = head.next
    return head
