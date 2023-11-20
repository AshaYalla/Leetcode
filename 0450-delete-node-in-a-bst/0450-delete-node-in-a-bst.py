# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        ans = root
        if root == None:
            return root
        def helper(ele):
            if ele.val == key:
                if ele.left and ele.right:
                    node = ele.left
                    while(node.right):
                        node = node.right
                    node.right = ele.right
                    return ele.left
                elif ele.left:
                    return ele.left
                else:
                    return ele.right
        if root.val == key:
            return helper(root)
                      
        while(root):
                
            if root.val > key:
                if root.left!= None and root.left.val == key:
                    root.left = helper(root.left)
                    return ans
                    break
                root = root.left
                
            else:
                if root.right!= None and root.right.val == key:
                    root.right = helper(root.right)
                    return ans
                    break
                root = root.right
        return ans
                
            
                
        