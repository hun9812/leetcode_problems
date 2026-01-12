# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head
        temp = head
        res = head.next
        connect = head.next.next
        res.next = temp
        temp.next = connect
        self.swapCount(head)
        return res

    def swapCount(self, node):
        if node is None:
            return
        if node.next is None:
            return
        if node.next.next is None:
            return
        first = node.next
        second = node.next.next
        third = second.next
        
        node.next = second
        second.next = first
        first.next = third
        self.swapCount(first)
        