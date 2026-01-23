# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:



        def check_valid(node, min_limit, max_limit):
            if node is None:
                return True
            check = True
            if node.val <= min_limit or node.val >= max_limit:
                return False
            if node.left is not None:
                check = check and check_valid(node.left, min_limit, node.val)
            if node.right is not None:
                check = check and check_valid(node.right, node.val, max_limit)
            return check
        
        return check_valid(root, -2**31-1, 2**31 )
        