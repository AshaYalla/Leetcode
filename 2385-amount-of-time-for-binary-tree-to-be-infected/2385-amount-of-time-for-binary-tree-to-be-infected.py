# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        dictt = defaultdict(list)
        q = [root]
        while(q):
            n = q.pop()
            if n:
                if n.left:
                    
                    q.append(n.left)
                    dictt[n.val].append(n.left.val)
                    dictt[n.left.val].append(n.val)
                if n.right:
                    q.append(n.right)
                    dictt[n.val].append(n.right.val)
                    dictt[n.right.val].append(n.val)
        print(dictt)    
        q = [start]
        visited = set()
        ans = 0
        while(q):
            
            ans+=1
            
            for i in range(len(q)):
                n = q.pop(0)
                if n not in visited:
                    visited.add(n)
     
                    for j in dictt[n]:
                        if j not in visited:
                            q.append(j)
        return ans - 1
                
            
            
        