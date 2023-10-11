# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(x, y):
            if x == []:
                return 
            ans = []
            nxtt = []
            for i in x:
                if i:
                    ans.append(i.val)
                    nxtt.append(i.left)
                    nxtt.append(i.right)
            if ans!= []:
                if y%2 == 0:
                    res.append(ans[::-1])
                else:
                    res.append(ans)
                
            dfs(nxtt,y+1)
            
        dfs([root], 1)
        return res
            
        