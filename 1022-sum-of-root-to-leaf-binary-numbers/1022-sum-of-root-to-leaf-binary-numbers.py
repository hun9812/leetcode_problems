# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root, 0)
        return self.res

    
    def dfs(self, node, cur_sum):
        if node is None:
            return
        
        cur_sum = cur_sum << 1
        cur_sum += node.val
        print(node.val, cur_sum)

        if node.left is None and node.right is None:
            self.res += cur_sum

        self.dfs(node.left, cur_sum)
        self.dfs(node.right, cur_sum)