"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        queue = deque()
        queue.append(root)
        while queue:
            lst = deque()
            for i in range(len(queue)):
                if queue[i]:
                    if i != len(queue) - 1:
                        queue[i].next = queue[i+1]
                    else:
                        queue[i].next = None
                    if queue[i].left:
                        lst.append(queue[i].left)
                    else:
                        lst.append(None)
                    if queue[i].right:
                        lst.append(queue[i].right)
                    else:
                        lst.append(None)
            queue = lst
        return root