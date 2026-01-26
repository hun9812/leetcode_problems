# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = []
        q.append([root, 0])
        if root is None:
            return []

        while q:
            cur = q.pop(0)
            if len(res) <= cur[1]:
                res.append([])
            res[cur[1]].append(cur[0].val)
            
            if cur[0].left is not None:
                q.append([cur[0].left, cur[1]+1])
            if cur[0].right is not None:
                q.append([cur[0].right, cur[1]+1])
        
        for i in range(len(res)):
            if i % 2 == 1:
                res[i] == res[i].reverse()
        return res
        