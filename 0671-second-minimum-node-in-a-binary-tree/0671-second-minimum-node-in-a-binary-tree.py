# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        min_node = root.val
        second_min = 2**31
        q = [root]
        
        while q:
            cur = q.pop(0)
            if cur is None:
                continue
            if cur.val > min_node and cur.val < second_min:
                second_min = cur.val
            q.append(cur.left)
            q.append(cur.right)
        
        if second_min == 2**31:
            return -1
        else:
            return second_min
        