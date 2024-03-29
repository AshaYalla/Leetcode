class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        
        parent = [i for i in range(len(edges)+1)]
        rank = [1] * len(parent)
        
        
        def findparent(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(i,j):
            pi = findparent(i)
            pj = findparent(j)
            
            if pi == pj:
                return False
            
            if rank[pi] > rank[pj]:
                parent[pi] = pj
                rank[pj]+= rank[pi]
            else:
                parent[pj] = pi
                rank[pi]+= rank[pj]
            return True
        
        # create a adjacency list. 
        graph = defaultdict(list)    
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        # dictt to track the common value nodes
        dictt = defaultdict(list)
        res = 0
        for i,j in enumerate(vals):
            dictt[j].append(i)
        
        # find if they belong to same set using union find
        for val in sorted(dictt.keys() ):
            for node in dictt[val]:
                for nei in graph[node]:
                    if vals[nei] <= vals[node]:
                        union(node,nei)
            counter = defaultdict(int)
            
            #find the parent of each node and if they belong to same set increment the result accordingly
            for node in dictt[val]:
                par = findparent(node)
                counter[par]+=1
                res+= counter[par]
        return res
            
            
            
        