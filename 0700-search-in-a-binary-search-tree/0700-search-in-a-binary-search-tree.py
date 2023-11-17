# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.val == val:
            return root
        if root.val < val:
            root = self.searchBST( root.right,val)
        else:
            root = self.searchBST(root.left,val)
            
        return root
#         if root is None or val == root.val:
#         return root

#        if val < root.val:
#              return self.searchBST(root.left, val) 
#         else:
#             return self.searchBST(root.right, val)
        
        
        
        # while(root!=None and root.val!= val):
        #     if root.val < val:
        #         root = root.right
        #     else:
        #         root = root.left
        # return root
    
            
        