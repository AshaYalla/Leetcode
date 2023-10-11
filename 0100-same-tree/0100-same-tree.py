class Solution:
    def isSameTree(self,p, q) -> bool:
        def dfs(x,y):
            if x == None and y == None:
                return True
            if x == None and y != None:
                return False
            if x != None and y == None:
                return False
            
            
            
            if x.val != y.val:
                return False
            l = dfs(x.left, y.left)
            r = dfs(x.right,y.right)
            return l and r
        return dfs(p,q)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if p==None and q==None:
#             return True
#         elif p==None or q==None:
#             return False

#         que_p=deque([p])
#         que_q=deque([q])

#         while(que_p):
#             node_p=que_p.pop()
#             node_q=que_q.pop()

#             if  node_p.left!=None and node_q.left==None or node_p.left==None and node_q.left !=None:
#                 return False
#             if node_p.right!=None and node_q.right==None or node_p.right==None and node_q.right !=None:
#                 return False
#             if node_p.val!= node_q.val:
#                 return False
            
#             if node_p.left and node_q.left:
#                 que_p.append(node_p.left)
#                 que_q.append(node_q.left)
#             if node_p.right and node_q.right:
#                 que_p.append(node_p.right)
#                 que_q.append(node_q.right)
#         return True