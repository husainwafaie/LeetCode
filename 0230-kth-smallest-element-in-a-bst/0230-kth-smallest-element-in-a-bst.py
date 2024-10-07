# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(r, num):
            if not r:
                return num
            if r.left:
                n = helper(r.left, num)
                if type(n) == int: 
                    num = n
                else:
                    return n
            num -= 1
            if num == 0:
                return r
            return helper(r.right, num)
            

        kth = helper(root, k)
        return kth.val