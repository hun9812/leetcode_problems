# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.val_count = []
        self.val_sum = []
        # root level을 0로 set
        self.calLevels(root, 0)

        for i in range(len(self.val_sum)):
            self.val_sum[i] /= self.val_count[i]
        
        return self.val_sum
        
    def calLevels(self, node, level):
        if node is None:
            return
        if len(self.val_count) <= level:
            self.val_count.append(1)
            self.val_sum.append(node.val)
        else:
            self.val_count[level] += 1
            self.val_sum[level] += node.val
        
        self.calLevels(node.left, level+1)
        self.calLevels(node.right, level+1)



        