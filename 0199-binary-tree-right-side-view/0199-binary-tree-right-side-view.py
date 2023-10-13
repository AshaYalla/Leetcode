# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        q = [root]
        res = []
        while(q):
            ans = []
            for i in range(len(q)):
                
                ele = q.pop(0)
                if(ele):
                    ans.append(ele.val)
                    q.append(ele.left)
                    q.append(ele.right)
            if ans:
                res.append(ans[-1])
        return res
                    
                    
                
            
        