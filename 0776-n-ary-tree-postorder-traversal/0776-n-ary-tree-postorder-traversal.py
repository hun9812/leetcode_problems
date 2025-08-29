"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.res = []
        if root is None:
            return self.res
        else:
            self.postTraverse(root)

        return self.res
    
    def postTraverse(self, node):
        if node is None:
            return
        
        for i in node.children:
            self.postTraverse(i)
        self.res.append(node.val)