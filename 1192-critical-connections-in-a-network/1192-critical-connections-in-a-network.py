class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)
        
        self.timer = 0
        intime = [0]*n
        lowtime = [0]*n
        visited = set()   
        ans = []
        def dfs(curr, parent):
            visited.add(curr)
            self.timer+=1
            intime[curr] = lowtime[curr] = self.timer
            for i in graph[curr]:
                if i not in visited:
                    dfs(i,curr)
                    lowtime[curr] = min(lowtime[curr], lowtime[i])
                else:
                    if i!=parent:
                        lowtime[curr] = min(lowtime[curr], lowtime[i])
                if intime[curr] < lowtime[i]:
                    ans.append([curr,i])
        dfs(0,-1)
        return ans
                
            
        