import heapq

# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0)
        cur = res
        heap = []

        for i, node in enumerate(lists):
            if node is None:
                continue
            heapq.heappush(heap, (node.val, i, node))
        
        while heap:
            cur_val, i, node = heapq.heappop(heap)
            
            new_node = ListNode(cur_val)
            cur.next = new_node
            cur = cur.next

            if node.next is not None:
                node = node.next
                heapq.heappush(heap, (node.val, i, node))
        
        return res.next