# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        que = [(root,0,0)]
        
        nodes = []
        
        while(que):
            ele,lev,ver = que.pop()
            if ele:
                nodes.append((lev,ver,ele.val))
                que.append((ele.left, lev -1, ver+1))
                que.append((ele.right, lev +1, ver+1))
        
        nodes.sort()
  
        
        dictt = defaultdict(list)
        
        for i,j,ele in nodes:
            dictt[i].append(ele)
        return dictt.values()
            
            
            
        