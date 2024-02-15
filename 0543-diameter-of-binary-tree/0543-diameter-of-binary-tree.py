# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.maxx = 0
        
        def solve(root):
            if not root:
                return -1
            if root:
                l = solve(root.left) +1
                r = solve(root.right) + 1
            self.maxx = max(self.maxx, l+r)
            return max(l,r)
        solve(root)
        return self.maxx
            
            