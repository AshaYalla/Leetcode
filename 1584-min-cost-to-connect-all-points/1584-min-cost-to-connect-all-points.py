class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        rank = [0]*n
        parent = [i for i in range(n)]
        
        def findparent(x):
            if parent[x] == x:
                return x
            parent[x] = findparent(parent[x])
            return parent[x]
            
        
        edges = []

        for i in range(n):
            for j in range(i+1,n):
                edges.append([abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]),i,j])
        edges.sort()
        cost = 0
        
        for dis, i, j in edges:
            pi = findparent(i)
            pj = findparent(j)
            if pi != pj:
                if rank[pi] == rank[pj]:
                    rank[pi]+=1
                    parent[pj] = pi
                elif rank[pi] > rank[pj]:
                    parent[pj] = pi
                else:
                    parent[pi] = pj
                cost+=dis
        return cost
                    
            
                
        