# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.check = root.val
        left_c = self.searchTree(root.left)
        right_c = self.searchTree(root.right)
        
        if left_c and right_c:
            return True
        else:
            return False

    def searchTree(self, node):
        if node is None:
            return True
        if node.val != self.check:
            return False
        l = self.searchTree(node.left)
        r = self.searchTree(node.right)
        if l and r:
            return True
        else:
            return False
        