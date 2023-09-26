class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        intime = [-1] * n
        lowtime = [-1] * n
        visited = set()
        self.timer = 0
        answer = []
        
        for (u,v) in connections:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(curr, par):
            visited.add(curr)
            self.timer+=1
            intime[curr] = lowtime[curr] = self.timer
            
            for i in graph[curr]:
                if i not in visited:
                    dfs(i, curr)
                    lowtime[curr] = min(lowtime[curr], lowtime[i])
                else:
                    if(i != par):
                        lowtime[curr] = min(intime[i], lowtime[curr])
                if(intime[curr] < lowtime[i]):
                    answer.append([curr,i])
        dfs(0,-1)  
        print(intime,lowtime)
        return answer       
            