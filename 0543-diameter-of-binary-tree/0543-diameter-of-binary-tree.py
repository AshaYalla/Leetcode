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
        def dfs(x):
            if x is None:
                return -1
            if x:
                l = dfs(x.left) + 1
                r = dfs(x.right) + 1
                self.maxx = max(self.maxx, l+r)
                return max(l,r)
        dfs(root)
        return self.maxx
                

            