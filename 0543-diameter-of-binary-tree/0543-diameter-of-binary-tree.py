# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.height(root)
        return self.res

    
    def height(self, node):
        if node is None:
            return 0
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        self.res = max(self.res, left_height+right_height)

        return max(left_height, right_height)+1
        