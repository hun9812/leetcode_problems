# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        return self.invertbinary(root)

    def invertbinary(self, node):
        if node is None:
            return None
        
        temp = node.right
        node.right = self.invertbinary(node.left)
        node.left = self.invertbinary(temp)
        return node
        