# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []
        if root is None:
            return res
        
        if root.left is None and root.right is None:
            self.res.append("{0}".format(root.val))
        if root.left is not None:
            self.rememberTree(root.left, "{0}".format(root.val))
        if root.right is not None:
            self.rememberTree(root.right, "{0}".format(root.val))
        return self.res


    def rememberTree(self, node, s):
        s += "->{0}".format(node.val)
        if node.left is None and node.right is None:
            self.res.append(s)
        if node.left is not None:
            self.rememberTree(node.left, s)
        if node.right is not None:
            self.rememberTree(node.right, s)