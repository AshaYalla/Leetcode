# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if len(inorder) == 0 or len(postorder) == 0:
            return None
        root = postorder[-1]
        ind = inorder.index(root)
        node = TreeNode(root)
        node.left = self.buildTree(inorder[:ind], postorder[:ind])
        node.right = self.buildTree(inorder[ind+1:], postorder[ind:-1])
        return node
        