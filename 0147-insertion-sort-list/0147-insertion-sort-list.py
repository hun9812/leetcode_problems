# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp_head = ListNode(-5001, next = head)


        def insert_node(head, node):
            prev = head
            while prev.next:
                if prev.next.val > node.val:
                    node.next = prev.next
                    prev.next = node
                    return
                prev = prev.next
        
        last_sorted = head
        cur = head.next
        while cur is not None:
            if cur.val >= last_sorted.val:
                last_sorted = last_sorted.next
            else:
                last_sorted.next = cur.next
                insert_node(temp_head, cur)
            cur = last_sorted.next
        
        return temp_head.next
        