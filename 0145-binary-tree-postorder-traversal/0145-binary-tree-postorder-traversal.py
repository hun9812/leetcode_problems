# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        self.postorder(root, res)
        return res
    
    def postorder(self, node, res):
        if node is None:
            return
        self.postorder(node.left, res)
        self.postorder(node.right, res)
        res.append(node.val)
        