# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dct = {}
        def dfs(r, curr, o):
            if not r:
                return
            if curr in dct:
                dct[curr].append([r.val, o])
            else:
                dct[curr] = [[r.val, o]]
            dfs(r.left, curr - 1, o + 1)
            dfs(r.right, curr + 1, o + 1)
        dfs(root, 0, 0)
        lst = []
        for i in sorted(dct.keys()):
            lst.append([i[0] for i in sorted(dct[i], key = lambda x:(x[1], x[0]))])

        return lst