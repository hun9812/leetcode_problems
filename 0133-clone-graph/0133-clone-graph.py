"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        cloned = {}

        def makeclone(cur_node):
            if cur_node in cloned:
                return cloned[cur_node]
            clone = Node(cur_node.val, [])
            cloned[cur_node] = clone
            for neighbor in cur_node.neighbors:
                clone_neighbors = makeclone(neighbor)
                clone.neighbors.append(clone_neighbors)
            return clone
        
        return makeclone(node)
