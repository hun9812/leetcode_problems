# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = None
        
        def bst_search(node):
            if node is None:
                return
            
            if node.left is not None:
                bst_search(node.left)
            self.count += 1
            #vprint(node.val, self.count)
            if self.count == k:
                self.res = node.val
                return
            if node.right is not None:
                bst_search(node.right)
        
        bst_search(root)
        return self.res