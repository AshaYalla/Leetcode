# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [p]
        stack2 = [q]

        while(stack):
            cur = stack.pop()
            cur2 = stack2.pop()   
            
            if((cur == None and cur2 != None) or (cur != None and cur2 == None)):
                return False
            
            if(cur and cur2):
                if(cur.val != cur2.val):
                    return False
                
                stack2.append(cur2.left)
                stack2.append(cur2.right)
                stack.append(cur.left)
                stack.append(cur.right)
            
        return True