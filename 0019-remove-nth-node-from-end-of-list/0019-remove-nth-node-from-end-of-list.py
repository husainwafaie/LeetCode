# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        curr = head
        while temp:
            temp = temp.next
            if n == -1:
                curr = curr.next
            else:
                n -= 1
        print(n)
        if curr == head and n == 0:
            return curr.next
        if n == 1:
            curr.next = None
        else:
            curr.next = curr.next.next
        return head