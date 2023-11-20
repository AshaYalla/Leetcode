# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        
        
        stack = [(float(-inf),root,float(inf))]
        while(stack):
            s, node, l = stack.pop(0)
            
            if node.val <= s or node.val >= l:
                return False
            if node.left:
                stack.append((s,node.left,node.val))
            if node.right:
                stack.append((node.val,node.right,l))
        return True
                
            