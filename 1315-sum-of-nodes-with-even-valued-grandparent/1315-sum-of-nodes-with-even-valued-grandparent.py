# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append([0, 0, root])
        total = 0
        while queue:
            item = queue.popleft()
            if item[0]:
                total += item[2].val
            item[0] = item[1]
            item[1] = 1 - (item[2].val % 2)
            if item[2].right:
                queue.append([item[0], item[1], item[2].right])
            if item[2].left:
                queue.append([item[0], item[1], item[2].left])
        return total