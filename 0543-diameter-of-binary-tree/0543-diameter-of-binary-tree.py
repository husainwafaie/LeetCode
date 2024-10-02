# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lst = []
        def helper(leaf):
            if not leaf:
                return 0
            if (not leaf.right and not leaf.left):
                return 1
            if not leaf.left:
                return 1 + helper(leaf.right)
            if not leaf.right:
                return 1 + helper(leaf.left)
            num1 = helper(leaf.right)
            num2 = helper(leaf.left)
            lst.append(num1 + num2)
            return 1 + max(num1, num2)
        
        lst.append(helper(root.right) + helper(root.left))
        return max(lst)