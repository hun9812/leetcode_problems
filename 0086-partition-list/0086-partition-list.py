# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_node = ListNode(0)
        rem_node = ListNode(0)
        res = smaller_node
        connect = rem_node

        while head is not None:
            if head.val < x:
                temp = head.next
                smaller_node.next = head
                smaller_node = smaller_node.next
                smaller_node.next = None
                head = temp
            else:
                temp = head.next
                rem_node.next = head
                rem_node = rem_node.next
                rem_node.next = None
                head = temp
            
        if res.next is None:
            return connect.next
        if connect.next is None:
            return res.next
        
        smaller_node.next = connect.next
        return res.next