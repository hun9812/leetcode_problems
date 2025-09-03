# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        self.mergeNode(root1, root2)

        return root1
        
    def mergeNode(self, node1, node2):
        if node1 is None:
            return node2
        if node2 is None:
            return node1
        
        node1.val += node2.val
        node1.left = self.mergeNode(node1.left, node2.left)
        node1.right = self.mergeNode(node1.right, node2.right)
        
        return node1


        