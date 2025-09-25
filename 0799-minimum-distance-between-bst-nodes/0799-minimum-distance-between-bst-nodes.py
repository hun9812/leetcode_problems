# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nodes = []
        q = [root]
        while q:
            cur = q.pop(0)
            nodes.append(cur.val)
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
        
        nodes.sort()
        res = 10**10
        for i in range(len(nodes)-1):
            res = min(res, nodes[i+1]-nodes[i])
        
        return res
        