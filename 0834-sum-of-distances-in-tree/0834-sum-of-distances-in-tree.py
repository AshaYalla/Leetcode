class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
          
        seen = set()
        seen.add(0)
        children = [0]*n
        self.summ = 0
        
        def dfs(node,level):
            total = 1
            self.summ+=level
            for i in graph[node]:
                if i not in seen:
                    seen.add(i)
                    total+=dfs(i,level+1)
            children[node] = total
            return total
       
        dfs(0,0)   
        seen = set()
        seen.add(0)
        res = [0] * n
        res[0] = self.summ
        
        def dfs2(node):
            for i in graph[node]:
                if i not in seen:
                    seen.add(i)
                    res[i] = res[node] - children[i] + (n - children[i] )
                    dfs2(i)
                    
        dfs2(0)
        return res
    
