# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {val: i for i, val in enumerate(inorder)}
        self.index = 0

        def make_inorder_tree(start, end):
            if start > end:
                return None
            root = TreeNode(preorder[self.index])
            mid = inorder_dict[preorder[self.index]]
            self.index += 1

            root.left = make_inorder_tree(start, mid-1)
            root.right = make_inorder_tree(mid+1, end)

            return root
        
        return make_inorder_tree(0, len(preorder)-1)