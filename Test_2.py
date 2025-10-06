class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head: 'Node') -> 'Node':
    if not head:
        return None

    # Step 1: Copy nodes and interweave them with original nodes
    curr = head
    while curr:
        copy = Node(curr.val)
        copy.next = curr.next
        curr.next = copy
        curr = copy.next

    # Step 2: Assign random pointers to the copied nodes
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Step 3: Separate the copied list from the original list
    curr = head
    dummy = Node(0)
    copy_curr = dummy

    while curr:
        copy = curr.next
        copy_curr.next = copy
        copy_curr = copy

        curr.next = copy.next  # Restore original list
        curr = curr.next

    return dummy.next
