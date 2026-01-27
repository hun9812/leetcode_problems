# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        total_length = 0
        temp = head
        while temp is not None:
            total_length += 1
            temp = temp.next

        def makeBST(node, length):
            # print(node.val, length)
            if node is None or length == 0:
                return None
            mid = length // 2
            temp = node
            while mid > 0:
                # print(length, temp.val)
                temp = temp.next
                mid -= 1

            root = TreeNode(temp.val)

            root.left = makeBST(node, length//2)
            root.right = makeBST(temp.next, length - (length//2) - 1)

            return root
        
        return makeBST(head, total_length)