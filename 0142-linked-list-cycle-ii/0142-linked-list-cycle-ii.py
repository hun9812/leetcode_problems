# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_set = set()
        k=0

        while head is not None:
            if head in node_set:
                return head
            else:
                node_set.add(head)
                head = head.next
        
        return head