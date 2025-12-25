# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1_leaf = []
        root2_leaf = []
        visited = set()
        self.dfs(root1, visited, root1_leaf)
        visited = set()
        self.dfs(root2, visited, root2_leaf)

        if len(root1_leaf) != len(root2_leaf):
            return False
        for i in range(len(root1_leaf)):
            if root1_leaf[i] != root2_leaf[i]:
                return False
        
        return True

    def dfs(self, cur, visited, root_leaf):
        if cur in visited:
            return
        if cur.left is None and cur.right is None:
            root_leaf.append(cur.val)
        if cur.right is not None:
            visited.add(cur)
            self.dfs(cur.right, visited, root_leaf)
        if cur.left is not None:
            visited.add(cur)
            self.dfs(cur.left, visited, root_leaf)