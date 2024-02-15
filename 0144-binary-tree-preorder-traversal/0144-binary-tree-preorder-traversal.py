# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = [root]
        
        
        while(stack):
            cur = stack.pop()
            if cur:
                ans.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)
        return ans
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        

#         ans = []
#         cur = root
#         while(cur!=None):
            
#             if cur.left == None:
#                 ans.append(cur.val)
#                 cur = cur.right
#             else:
#                 node = cur.left 
#                 while(node.right and node.right != cur):
#                     node = node.right
#                 if node.right == None:
#                     node.right = cur
#                     ans.append(cur.val)
#                     cur = cur.left
                    
#                 else:
#                     node.right = None
#                     cur = cur.right
#         return ans
        
        
#         res = []
        
#         def dfs(x):
#             if x:
#                 res.append(x.val)
#                 dfs(x.left)
                
#                 dfs(x.right)
                
                
                
            
            
#         dfs(root)
#         return res

#         res = []
#         stack = [root]

#         while stack:
#             ele = stack.pop()
#             if ele:
#                 res.append(ele.val)
                

#                 if ele.right:
#                     stack.append(ele.right)
#                 if ele.left:
#                     stack.append(ele.left)
#         return res
        
                
            
            
        