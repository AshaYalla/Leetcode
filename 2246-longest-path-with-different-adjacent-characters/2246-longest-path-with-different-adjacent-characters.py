class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:

        graph = defaultdict(list)
        for i in range(1,len(parent)):
            graph[parent[i]].append(i)
            graph[i].append(parent[i])
        
        seen = set()
        self.dia = 0
        
        def dfs(node):
            d1,d2 = 0,0
            
            for k in graph[node]:
                if k not in seen:
                    seen.add(k)
                    d = dfs(k)
                    if s[node]!= s[k]:
                        if d > d1:
                            d1,d2 = d,d1
                        elif d > d2:
                            d2 = d
                    
                        
                        
            self.dia = max(self.dia,d1+d2)
            return d1 + 1
        seen.add(0)
        dfs(0)
        return self.dia  + 1  
            
                    
            