# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return ListNode(val="")
        if len(lists) == 1:
            return lists[0]
        """
        r_num = 1
        while r_num < len(lists):
            l = lists[0]
            r = lists[r_num]
            if l == None:
                lists[0] = r
            elif r == None:
                pass
            else:
                while (l or r):
                    if l.next == None:
                        if l.val > r.val:
                            if r.next == None:
                                r.next = l
                                lists[0] = lists[r_num]
                                break
                            else:
                                if r.next.val > l.val:
                                    l.next = r.next
                                    r.next = l
                                    lists[0] = lists[r_num]
                                else:
                                    r = r.next
                        else:
                            l.next = r
                            break
                    elif r.next == None:
                        if l.next.val > r.val:
                            r.next = l.next
                            l.next = r
                            break
                        else:
                            l = l.next
                    else:
                        if l.val > r.val:
                            l2 = l.next
                            r.next = l.next

                            l = l2
                        elif l.next.val > r.val:
                            r2 = r.next
                            r.next = l.next
                            l.next = r
                            r = r2
                        else:
                            l = l.next
            r_num += 1
        return lists[0]
        """
        curr = ListNode(val="")
        ret = curr
        first = True
        while True:
            mval = float("inf")
            vindex = -1
            holder = False
            for i in range(len(lists)):
                if lists[i] != None:
                    holder = True
                    if lists[i].val < mval:
                        mval = lists[i].val
                        vindex = i
            if holder == False:
                break
            if first:
                curr.val = mval
                curr.next = None
                first = False
                lists[vindex] = lists[vindex].next
            else:
                curr.next = ListNode(val = mval)
                curr = curr.next
                lists[vindex] = lists[vindex].next
        return ret

        