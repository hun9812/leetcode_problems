# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.new_tree = TreeNode(0)
        self.cur = self.new_tree
        self.inorder(root)
        return self.new_tree.right

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)

        node.left = None
        self.cur.right = node
        self.cur = self.cur.right

        self.inorder(node.right)
        