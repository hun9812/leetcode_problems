# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []

        def cur_check(node, target, cur_list):
            # print(node.val, cur_list)
            if node is None:
                return
            if node.left is None and node.right is None:
                if node.val == target:
                    cur_list.append(target)
                    self.res.append(cur_list[:])
                    cur_list.pop()
                return
            cur_list.append(node.val)
            target -= node.val
            if node.left:
                cur_check(node.left, target, cur_list)
            if node.right:
                cur_check(node.right, target, cur_list)
            cur_list.pop()
            target += node.val
            return
        
        cur_check(root, targetSum, [])
        return self.res