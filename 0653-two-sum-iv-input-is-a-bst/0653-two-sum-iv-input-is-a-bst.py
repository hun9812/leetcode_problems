# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dict = {}
        q = [root]
        while q:
            cur = q.pop(0)
            if cur is None:
                continue
            dict[cur.val] = True
            q.append(cur.left)
            q.append(cur.right)
        
        print(dict)
        for i in dict.keys():
            if (k-i) in dict:
                if k-i == i:
                    continue
                return True
        
        return False

        