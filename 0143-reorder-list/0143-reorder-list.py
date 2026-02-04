# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node_dict = {}

        if head.next is None:
            return head
        
        temp = head.next
        k = 1
        while temp is not None:
            node_dict[k] = temp
            k += 1
            temp = temp.next
        node_dict[0] = None
        
        u = 1
        for i in range(1, k):
            # 총노드는 k-1개가 있음
            if i % 2 == 1:
                head.next = node_dict[k-u]
                head = head.next
            else:
                head.next = node_dict[u]
                head = head.next
                u += 1
        
        head.next = None
