# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        lst = []
        queue = deque()
        queue.append(root)
        mode = False
        while queue:
            l = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if not mode:
                    l.append(node.val)
                else:
                    l.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            mode = not mode
            lst.append(l)
        return lst