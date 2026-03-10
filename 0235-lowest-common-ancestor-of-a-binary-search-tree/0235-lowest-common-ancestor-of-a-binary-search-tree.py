# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        def find_LCA(node):
            if node is None:
                return
            if node.val == p.val or node.val == q.val:
                self.res = node
                return
            elif node.val >= p.val and node.val >= q.val:
                self.res = node
                find_LCA(node.left)
            elif node.val <= p.val and node.val <= q.val:
                self.res = node
                find_LCA(node.right)
            elif node.val >= p.val and node.val <= q.val:
                self.res = node
                return
            elif node.val <= p.val and node.val >= q.val:
                self.res = node
                return
        find_LCA(root)
        return self.res