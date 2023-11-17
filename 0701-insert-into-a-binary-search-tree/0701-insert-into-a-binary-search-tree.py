# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            root = TreeNode(val)
            return root
        ans = root
        while(root!= None):
            if root.val > val:
                if root.left == None:
                    root.left = TreeNode(val)
                    break
                root = root.left 
                
            else:
                if root.right == None:
                    root.right = TreeNode(val)
                    break
                root = root.right
                
        return ans
        