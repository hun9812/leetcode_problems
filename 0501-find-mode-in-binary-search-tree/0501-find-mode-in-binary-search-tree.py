# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dict = {}
        self.traverse(root)

        self.sorted_dict = sorted(self.dict.items(), key = lambda x :x[1], reverse = True)
        res = [self.sorted_dict[0][0]]
        for i in range(1,len(self.sorted_dict)):
            if self.sorted_dict[i][1] == self.sorted_dict[i-1][1]:
                res.append(self.sorted_dict[i][0])
            else:
                break
        return res


    def traverse(self, node):
        if node is None:
            return

        if node.val in self.dict:
            self.dict[node.val] += 1
        else:
            self.dict[node.val] = 1

        self.traverse(node.left)
        self.traverse(node.right)
        