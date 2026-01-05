# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.low = low
        self.high = high
        self.res = 0
        if root is None:
            return self.res
        self.searchBST(root)
        return self.res

    def searchBST(self, node):
        if node is None:
            return
        if node.val >= self.low and node.val <= self.high:
            self.res += node.val
        self.searchBST(node.left)
        self.searchBST(node.right)

        