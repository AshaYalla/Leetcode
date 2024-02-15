# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def demo(root):
            if root:
                if root.left:
                    demo(root.left)

                ans.append(root.val)
                if root.right:
                    demo(root.right)
            
        demo(root)
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
#                     cur = cur.left
#                 else:
#                     node.right = None
#                     ans.append(cur.val)
#                     cur = cur.right
#         return ans
        
        
        
#         ans = []
#         cur = root
#         while cur != None:
#             #printing the leftmost node
#             if not cur.left:
#                 ans.append(cur.val)
#                 cur = cur.right
#             else:
#                 temp = cur
#                 temp = temp.left
#                 #going to the rightmost node in the left subtree (lets call it temp)
#                 while temp.right and temp.right != cur:
#                     temp = temp.right
                
#                 #2 conditions arise:
                
#                 #i. the right child of temp doesn't exist (The thread to the cur node has not been made)
#                 #in this case, point the right child of temp to cur and move cur to its left child
#                 if not temp.right:
#                     temp.right = cur
#                     cur = cur.left

#                 #ii. the thread has already been created so we break the thread
#                 #(pointing the temp's right child back to None)and print cur.
#                 #Finally, move cur to its right child      
#                 else:
#                     ans.append(cur.val)
#                     temp.right = None
#                     cur = cur.right

#         return ans


# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
        
#         def dfs(x):
#             if x:
#                 dfs(x.left)
#                 res.append(x.val)
#                 dfs(x.right)
                
                
            
            
#         dfs(root)
#         return res
            
#         res = []
#         stack = []
#         node = root
        
#         while(stack or node):
#             while(node):
#                 stack.append(node)
#                 node = node.left
#             ele = stack.pop()
#             res.append(ele.val)
#             node = ele.right
#         return res
            
                


        