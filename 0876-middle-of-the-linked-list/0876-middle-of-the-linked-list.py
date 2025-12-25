# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        dup = head
        while head is not None:
            length += 1
            head = head.next
        
        length //= 2
        for i in range(length):
            dup = dup.next
        
        return dup
        