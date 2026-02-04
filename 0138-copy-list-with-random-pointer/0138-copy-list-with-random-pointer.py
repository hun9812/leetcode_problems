"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_dict = {}
        if head is None:
            return None

        def copy_next(node):
            if node is None:
                return None
            if node in node_dict:
                return node_dict[node]
            
            new_node = Node(node.val)
            node_dict[node] = new_node

            new_node.next = copy_next(node.next)

            return new_node
        
        copy_next(head)
        temp = head
        while temp is not None:
            if temp.random is None:
                temp = temp.next
                continue
            
            node_dict[temp].random = node_dict[temp.random]
            temp = temp.next
        
        return node_dict[head]