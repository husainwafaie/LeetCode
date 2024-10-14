# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        lst = []
        def dfs(r, num, l):
            if not r:
                return
            if num + r.val == targetSum and not r.left and not r.right:
                l.append(r.val)
                lst.append(l.copy())
                l.pop()
                return
            l.append(r.val)
            dfs(r.left, num + r.val, l)
            dfs(r.right, num + r.val, l)
            l.pop()
            return
        dfs(root, 0, [])
        return lst
            