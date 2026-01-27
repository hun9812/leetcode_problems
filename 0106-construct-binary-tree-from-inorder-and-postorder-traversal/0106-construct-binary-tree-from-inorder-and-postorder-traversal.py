# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {val: i for i, val in enumerate(inorder)}
        self.index = len(postorder)-1

        def make_inorder_tree(start, end):
            if start > end:
                return None
            root = TreeNode(postorder[self.index])
            mid = inorder_dict[postorder[self.index]]
            self.index -= 1

            root.right = make_inorder_tree(mid+1, end)
            root.left = make_inorder_tree(start, mid-1)
            

            return root
        
        return make_inorder_tree(0, len(postorder)-1)