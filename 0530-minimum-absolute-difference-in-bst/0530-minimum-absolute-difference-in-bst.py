# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.nodes = []
        self.findNodes(root)

        self.nodes.sort()
        self.res = 10**5
        for i in range(len(self.nodes)-1):
            self.res = min(self.res, self.nodes[i+1] - self.nodes[i])
        
        return self.res

    def findNodes(self, node):
        if node is None:
            return
        self.nodes.append(node.val)

        self.findNodes(node.left)
        self.findNodes(node.right)
        