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
                x = stack.pop(0)
                if x:
                    level.append(x.val)
                    stack.append(x.left)
                    stack.append(x.right)
            if level:
                ans.append(level)
        return ans
                
                
                
        
        
        # ans = []
        # def dfs(curr):
        #     level = []
        #     nextt = []
        #     for x in curr:
        #         if x:
        #             level.append(x.val)
        #             nextt.append(x.left)
        #             nextt.append(x.right)
        #     if level:
        #         ans.append(level)
        #     if nextt:
        #         dfs(nextt)
        # dfs([root])
        # return ans
                    
                
            
        
        
        
        
        
        

        
        
        
        
        
#         res = []
#         def dfs(curr):
#             ans = []
#             nextt = []
#             for x in curr:
#                 if x:
#                     ans.append(x.val)
#                     nextt.append(x.left)
#                     nextt.append(x.right)
#             if ans:
#                 res.append(ans)
#             if nextt:
#                 dfs(nextt)
#         dfs([root])
#         return res
    
        
        
        
        # stack = [root]
        # result = []
        # while(stack):
        #     level = []
        #     slen = len(stack)
        #     for i in range(slen):
        #         cur = stack.pop(0)
        #         if(cur):
        #             level.append(cur.val)
        #             stack.append(cur.left)
        #             stack.append(cur.right)
        #     if(level):
        #         result.append(level)
        # return result
                
                
            
        
            
                   
        