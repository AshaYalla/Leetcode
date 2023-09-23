class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        redundency = 0
        parent = [i for i in range(n)]
        def findp(x):
            if x!= parent[x]:
                parent[x] = findp(parent[x])
            return parent[x]
        
        
        for i,j in connections:
            pi = findp(i) 
            pj = findp(j)
            if pi == pj:
                redundency +=1
            else:
                parent[pj] = pi
        
        count = 0
        
                
        for i in range(len(parent)) :
            if i == parent[i]:
                count+=1
        count -=1
        
        
        if redundency < count:
            return -1
        return count
                
                
                
        
        