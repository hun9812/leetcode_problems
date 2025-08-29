"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.res = []
        if root is None:
            return self.res
        else:
            self.preTraverse(root)

        return self.res
    
    def preTraverse(self, node):
        if node is None:
            return
        self.res.append(node.val)
        for i in node.children:
            self.preTraverse(i)
        