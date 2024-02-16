# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #stack - max, min
        stack = [(root, float('inf'), float('-inf'))]
        while(stack):
            node,maxx,minn = stack.pop()
            if node:
                if node.val >= maxx or node.val <= minn:
                    return False
                stack.append((node.left, node.val,minn))
                stack.append((node.right,maxx, node.val))
        return True
        
                 
            
            