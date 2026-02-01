# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfssum(node, cur_sum):
            if node is None:
                return
            if node.left is None and node.right is None:
                cur_sum.append(str(node.val))
                self.res += int("".join(cur_sum))
                cur_sum.pop()
                return
            cur_sum.append(str(node.val))
            dfssum(node.left, cur_sum)
            dfssum(node.right, cur_sum)
            cur_sum.pop()
        
        dfssum(root, [])
        return self.res
        