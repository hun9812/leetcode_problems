# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        check = []
        while head is not None:
            check.append(head.val)
            head = head.next
        
        if not check:
            return True

        for i in range(len(check)//2+1):
            if check[i] != check[-(i+1)]:
                return False
        
        return True
        