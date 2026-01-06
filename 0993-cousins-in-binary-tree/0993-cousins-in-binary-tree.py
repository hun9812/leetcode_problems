# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        res_x = []
        res_y = []
        q = [[root, None, 0]]
        while q:
            cur = q.pop(0)
            if cur[0] is None:
                continue
            if cur[0].val == x:
                res_x = cur
            if cur[0].val == y:
                res_y = cur
            if cur[0].left is not None:
                q.append([cur[0].left,cur[0],cur[2]+1])
            if cur[0].right is not None:
                q.append([cur[0].right, cur[0], cur[2]+1])
        
        if res_x[2] == res_y[2]:
            if res_x[1] != res_y[1]:
                return True
        return False
        