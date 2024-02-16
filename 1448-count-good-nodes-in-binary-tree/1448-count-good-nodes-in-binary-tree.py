# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(x, maxx):
            if x == None:
                return 
            
            if x:
                if x.val >= maxx:
                    maxx = x.val
                    self.ans +=1   

                dfs(x.left, maxx)
                dfs(x.right, maxx)
        dfs(root,float("-inf") )
        return self.ans