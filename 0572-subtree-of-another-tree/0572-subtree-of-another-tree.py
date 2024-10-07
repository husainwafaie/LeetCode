# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            if not subRoot:
                return True
            return False
        lst = []
        def find(t, num):
            if not t:
                return
            if t.val == num:
                lst.append(t)
            find(t.left, num)
            find(t.right, num)
        temp = root
        find(temp, subRoot.val)
        def helper(r1, r2):
            if not r1 and not r2:
                return True
            elif not r1 or not r2:
                return False
            elif r1.val != r2.val:
                return False
            return helper(r1.left, r2.left) and helper(r1.right, r2.right)
        for i in lst:
            if helper(i, subRoot):
                return True
        return False
        