# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        newHead = ListNode(-101)
        build = newHead
        slow = head
        fast = head
        count = 0
        while slow is not None:
            while fast is not None and fast.val == slow.val:
                count += 1
                fast = fast.next
            if count is 1:
                build.next = ListNode(slow.val)
                build = build.next
            slow = fast
            count = 0

        return newHead.next
