# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dict = {}
        while headA is not None:
            dict[headA] = True
            headA = headA.next
        
        while headB is not None:
            if headB in dict:
                return headB
            else:
                headB = headB.next
        
        return None