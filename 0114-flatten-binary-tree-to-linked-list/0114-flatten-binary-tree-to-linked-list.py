# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        self.pre_order_list = []
        
        def pre_order(node):
            if node is None:
                return
            self.pre_order_list.append(node)
            pre_order(node.left)
            pre_order(node.right)
        
        pre_order(root)
        root.left = None
        prev = root
    
        for i in range(1, len(self.pre_order_list)):
            self.pre_order_list[i].left = None
            self.pre_order_list[i].right = None
            prev.right = self.pre_order_list[i]
            prev = self.pre_order_list[i]
        
        return root