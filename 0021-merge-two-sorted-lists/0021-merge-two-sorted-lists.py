# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        r1 = list1
        r2 = list2
        if list2.val > list1.val:
            start = list1
            r1 = r1.next
        else:
            start = list2
            r2 = r2.next
        ret = start
        while r1 or r2:
            if not r1:
                start.next = r2
                return ret
            if not r2:
                start.next = r1
                return ret
            if r1.val > r2.val:
                start.next = r2
                r2 = r2.next
            else:
                start.next = r1
                r1 = r1.next
            start= start.next
        return ret
        