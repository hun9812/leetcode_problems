# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        temp = ListNode(0)
        res = temp

        while head is not None:
            if head.next is None:
                new_node = ListNode(head.val)
                temp.next = new_node
                break

            if head.val == head.next.val:
                cur_val = head.val
                while head is not None and head.val == cur_val:
                    head = head.next
            else:
                new_node = ListNode(head.val)
                temp.next = new_node
                temp = temp.next
                head = head.next

        return res.next