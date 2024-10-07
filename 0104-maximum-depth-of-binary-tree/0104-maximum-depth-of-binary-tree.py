# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def helper(r):
            if r.left and r.right:
                return 1 + max(helper(r.left), helper(r.right))
            elif r.right:
                return 1 + helper(r.right)
            elif r.left:
                return 1 + helper(r.left)
            else:
                return 0
        return 1 + helper(root)