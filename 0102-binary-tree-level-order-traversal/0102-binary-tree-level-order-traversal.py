# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [root]
        result = []
        while(stack):
            level = []
            slen = len(stack)
            for i in range(slen):
                cur = stack.pop(0)
                if(cur):
                    level.append(cur.val)
                    stack.append(cur.left)
                    stack.append(cur.right)
            if(level):
                result.append(level)
        return result
                
                
            
        
            
                   
        