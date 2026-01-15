# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return
        tail = head
        l = 1
        while tail.next is not None:
            tail = tail.next
            l += 1
        
        k = k % l
        if k == 0:
            return head

        aim = l - k
        new_tail = head
        for _ in range(aim-1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        return new_head