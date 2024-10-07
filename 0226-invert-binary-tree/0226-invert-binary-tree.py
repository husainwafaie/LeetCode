# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        def helper(r):
            if not r or (not r.left and not r.right):
                return
            r.left, r.right = r.right, r.left
            helper(r.left)
            helper(r.right)
        
        helper(root)
        return root