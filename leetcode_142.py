class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Floyd Cycle Algorithm
def detect_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
