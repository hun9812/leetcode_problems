# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.not_ok_1 = self.not_ok_2 = self.prev = None

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            if self.prev is not None and self.prev.val > node.val:
                if self.not_ok_1 is None:
                    self.not_ok_1 = self.prev
                
                self.not_ok_2 = node
            self.prev = node
            inorder(node.right)
        
        inorder(root)
        self.not_ok_1.val, self.not_ok_2.val = self.not_ok_2.val, self.not_ok_1.val

        