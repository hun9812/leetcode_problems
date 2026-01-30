"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root

        while node is not None:
            dummy = Node(0)
            next_node = dummy
            prev = dummy
            while node is not None:
                if node.left:
                    prev.next = node.left
                    prev = node.left
                if node.right:
                    prev.next = node.right
                    prev = node.right
                node = node.next
            node = dummy.next
        
        return root