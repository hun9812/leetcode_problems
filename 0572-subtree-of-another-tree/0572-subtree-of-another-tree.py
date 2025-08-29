# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = [root]

        while q:
            cur = q.pop(0)
            if cur is None:
                continue
            if self.isSame(cur, subRoot):
                return True
            q.append(cur.left)
            q.append(cur.right)
        return False



    def isSame(self, node, subRoot):
        if node is None and subRoot is None:
            return True
        if node is None or subRoot is None:
            return False
        
        if (node.val == subRoot.val) and self.isSame(node.left, subRoot.left) and self.isSame(node.right, subRoot.right):
            return True
        else:
            return False
        