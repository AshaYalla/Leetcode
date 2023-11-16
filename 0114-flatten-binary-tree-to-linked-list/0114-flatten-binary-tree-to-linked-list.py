# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #morristraversal
        

        cur = root
        while(cur!=None):
            if cur.left == None:
                cur = cur.right
            else:
                node = cur.left 
                while(node.right and node.right != cur):
                    node = node.right
                if node.right == None:
                    node.right = cur.right
                    cur.right = cur.left
                    leftt = cur.left
                    cur.left = None
                    cur = leftt
                else:
                    node.right = None
                    cur = cur.right


        
        
        
#         stack = [root]
#         while stack:
#             cur = stack.pop()
#             if cur:
#                 if cur.right:
#                     stack.append(cur.right)
#                 if cur.left:
#                     stack.append(cur.left)
#                 if stack:
#                     cur.right = stack[-1]
#                 cur.left = None
        
        
#         self.prev = None
#         def flattens(root):
#             if root == None:
#                 return

#             cur = root
#             flattens(cur.right)
#             flattens(cur.left)

#             cur.left = None
#             cur.right = self.prev
#             self.prev = cur
#             return cur
#         flattens(root)
            
        