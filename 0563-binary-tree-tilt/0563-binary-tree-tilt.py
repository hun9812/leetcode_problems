# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.find_left_right_sum(root)

        res = 0
        q = [root]
        while q:
            cur = q.pop(0)
            if cur is None:
                continue
            res += cur.val
            q.append(cur.left)
            q.append(cur.right)
        
        return res

    
    def find_left_right_sum(self, node):
        if node is None:
            return 0
        
        left_sum = self.find_left_right_sum(node.left)
        right_sum = self.find_left_right_sum(node.right)

        diff = abs(left_sum-right_sum)
        ret_val = left_sum + right_sum + node.val

        node.val = diff

        return ret_val
        