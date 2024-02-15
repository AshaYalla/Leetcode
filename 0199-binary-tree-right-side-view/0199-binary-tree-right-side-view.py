# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        ans = []
        def dfs(curr):
            nextt = []
            for x in curr:
                if x:
                    if x.left:
                        nextt.append(x.left)
                    if x.right:
                        nextt.append(x.right)
                    right = x.val
            ans.append(right)

            if nextt:
                dfs(nextt)
        dfs([root])
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         q = [root]
#         res = []
#         while(q):
#             ans = []
#             for i in range(len(q)):
                
#                 ele = q.pop(0)
#                 if(ele):
#                     ans.append(ele.val)
#                     q.append(ele.left)
#                     q.append(ele.right)
#             if ans:
#                 res.append(ans[-1])
#         return res
                    
                    
                
            
        