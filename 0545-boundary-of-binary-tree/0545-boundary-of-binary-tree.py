# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        def leftside(node):
            if(not node or not node.left and not node.right):
                return
            res.append(node.val)
            if(node.left):
                leftside(node.left)
            elif(node.right):
                leftside(node.right)
        def rightside(node):
            if(not node or not node.left and not node.right):
                return
            if(node.right):
                rightside(node.right)
            elif(node.left):
                rightside(node.left)
 
            res.append(node.val)
        def leaves(node):
            if not node:
                return
            leaves(node.left)
            if(node != root and node.left is None and node.right is None):
                res.append(node.val)
            leaves(node.right)
            
        if(root is None):
            return []
        res = [root.val]    
        leftside(root.left)
        leaves(root)
        rightside(root.right)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#         def leftside(node):
#             if(not node or not node.left and not node.right):
#                 return
#             res.append(node.val)
#             if(node.left):
#                 leftside(node.left)
#             elif(node.right):
#                 leftside(node.right)
#         def rightside(node):
#             if(not node or not node.left and not node.right):
#                 return
#             if(node.right):
#                 rightside(node.right)
#             elif(node.left):
#                 rightside(node.left)
 
#             res.append(node.val)
#         def leaves(node):
#             if not node:
#                 return
#             leaves(node.left)
#             if(node != root and node.left is None and node.right is None):
#                 res.append(node.val)
#             leaves(node.right)
            
#         if(root is None):
#             return []
#         res = [root.val]    
#         leftside(root.left)
#         leaves(root)
#         rightside(root.right)
#         return res