class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if(len(edges)!=n-1):
            return False
        visited = set()
        queue = [0]
        graph = {i:[] for i in range(n)}
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        while(queue):
            cur = queue.pop(0)
            visited.add(cur)
            for i in graph[cur]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
        print(visited)
        return len(visited) == n
            
            
            
            