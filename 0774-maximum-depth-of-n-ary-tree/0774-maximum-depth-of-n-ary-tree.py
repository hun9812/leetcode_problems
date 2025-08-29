"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        self.res = self.findDepth(root, 1)

        return self.res
        

    
    def findDepth(self, node, cur_depth):
        if node is None:
            return cur_depth
        
        child_depth = cur_depth
        for i in node.children:
            cur_child = self.findDepth(i, cur_depth+1)
            child_depth = max(child_depth, cur_child)
        
        return child_depth
        