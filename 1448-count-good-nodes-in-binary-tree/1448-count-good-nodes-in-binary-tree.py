# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(r, num):
            n = 0
            if not r:
                return n
            if r.val >= num:
                n += 1
                num = r.val
            return n + helper(r.left, num) + helper(r.right, num)
        return helper(root, float("-inf"))