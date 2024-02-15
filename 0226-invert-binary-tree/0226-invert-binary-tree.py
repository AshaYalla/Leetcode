# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [(root,False)]
        while(stack):
            node, visited = stack.pop()
            
            if(node):
                if(visited):
                    node.left, node.right = node.right, node.left
                else:
                    stack.append((node,True))
                    stack.append((node.right,False))
                    stack.append((node.left,False))

        return root 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         stack = [root]
#         while(stack):
#             cur = stack.pop()
#             if cur:
#                 cur.left, cur.right = cur.right, cur.left
#                 stack.append(cur.left)
#                 stack.append(cur.right)
#         return root
            
        