# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        second = head.next
        ret = second
        prev = None
        while second:
            after = second.next
            head.next = after
            if prev:
                prev.next = second
            second.next = head
            prev = head
            head = prev.next
            if head:
                second = head.next
            else:
                second = None
        return ret
        