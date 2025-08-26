# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        while l1 is not None:
            num1 += str(l1.val)
            l1 = l1.next
        while l2 is not None:
            num2 += str(l2.val)
            l2 = l2.next
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        num1 = int(num1)
        num2 = int(num2)
        num3 = num1 + num2
        num3 = str(num3)[::-1]
        
        l3 = ListNode()
        
        temp = l3
        for i in range(len(num3)):
            temp.val = int(num3[i])
            if i == len(num3) - 1:
                temp.next = None
                continue
            new_node = ListNode()
            temp.next = new_node
            temp = temp.next
        
        return l3