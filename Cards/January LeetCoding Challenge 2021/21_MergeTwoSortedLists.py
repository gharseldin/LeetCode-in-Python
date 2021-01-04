# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # initial check
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # initialize return head and iterators
        walk1 = l1
        walk2 = l2
        head = ListNode()
        walk = head
        if l1.val < l2.val:
            walk.val = l1.val
            walk1 = walk1.next
        else:
            walk.val = l2.val
            walk2 = walk2.next

        # merge function
        while walk1 is not None and walk2 is not None:
            if walk1.val < walk2.val:
                walk.next = ListNode(walk1.val)
                walk1 = walk1.next
            else:
                walk.next = ListNode(walk2.val)
                walk2 = walk2.next
            walk = walk.next

        while walk1 is not None:
            walk.next = ListNode(walk1.val)
            walk1 = walk1.next
            walk = walk.next

        while walk2 is not None:
            walk.next = ListNode(walk2.val)
            walk2 = walk2.next
            walk = walk.next

        return head
