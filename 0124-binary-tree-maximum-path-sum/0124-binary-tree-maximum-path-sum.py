# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:


        self.maxx = -float('inf')
        
        def dfs(x):
            if x == None:
                return 0
            l = dfs(x.left)
            r = dfs(x.right)
            
            self.maxx = max(self.maxx, l+r+x.val)
            curr = max(l,r)+x.val
            self.maxx = max(curr, self.maxx,x.val)
            return max(l+x.val,r+x.val,x.val)
        dfs(root)
        return self.maxx
        