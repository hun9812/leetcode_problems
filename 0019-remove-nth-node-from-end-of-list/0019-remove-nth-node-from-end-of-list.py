# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_list = 0
        node = head
        while node is not None:
            len_list += 1
            node = node.next
        target = len_list - n
        
        node = head
        for i in range(target-1):
            node = node.next
        
        if n == 1:
            if len_list == 1:
                return None
            node.next = None
            return head
        
        if len_list == n:
            return head.next
    
        node.next = node.next.next
        return head