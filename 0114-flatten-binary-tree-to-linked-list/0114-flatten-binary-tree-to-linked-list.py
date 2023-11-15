# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        def flattens(root):
            if root == None:
                return

            cur = root
            flattens(cur.right)
            flattens(cur.left)

            cur.left = None
            cur.right = self.prev
            self.prev = cur
            return cur
        flattens(root)
            
        