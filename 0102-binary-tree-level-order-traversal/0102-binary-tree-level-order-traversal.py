# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [root]
        ans = []
        while(stack):
            level = []
            for i in range(len(stack)):
                node = stack.pop(0)
                if node: 
                    level.append(node.val) 
                    stack.append(node.left)
                    stack.append(node.right)
            if level:
                ans.append(level)
        return ans

            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        res = []
        def dfs(curr):
            ans = []
            nextt = []
            for x in curr:
                if x:
                    ans.append(x.val)
                    nextt.append(x.left)
                    nextt.append(x.right)
            if ans:
                res.append(ans)
            if nextt:
                dfs(nextt)
        dfs([root])
        return res
    
        
        
        
        stack = [root]
        result = []
        while(stack):
            level = []
            slen = len(stack)
            for i in range(slen):
                cur = stack.pop(0)
                if(cur):
                    level.append(cur.val)
                    stack.append(cur.left)
                    stack.append(cur.right)
            if(level):
                result.append(level)
        return result
                
                
            
        
            
                   
        