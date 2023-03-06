# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        stack = [(root,False)]
        res = []
        bleh = []
        maxx = -1
        
        while(stack):
            cur, visited = stack.pop()
            if cur:
                if(visited):
                    res.append(cur.val)
                    val = bleh.pop()
                    for i in bleh:
                        maxx = max(maxx,abs(i-val))

                else:
                    stack.append((cur,True))
                    bleh.append(cur.val)
                    stack.append((cur.right,False))
                    stack.append((cur.left,False))
        return maxx
                
                