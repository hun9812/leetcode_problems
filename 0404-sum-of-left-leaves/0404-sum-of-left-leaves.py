# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        if root.left is None and root.right is None:
            return self.res
        else:
            self.sumLeft(root, False)
        return self.res

    
    def sumLeft(self, node, amileft):
        if node.left is None:
            if node.right is None:
                if amileft:
                    self.res += node.val
                    return
                return
            self.sumLeft(node.right, False)
            return
        self.sumLeft(node.left, True)
        if node.right is not None:
            self.sumLeft(node.right, False)