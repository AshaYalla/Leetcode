class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
#         graph = defaultdict(list)
#         for i, j in connections:
#             graph[i].append((j))
#             graph[j].append((i))
            

#         self.visited = set()
#         self.ans = 0
        
#         def dfs(x):
#             for a in graph[x]:
#                 if a in self.visited:
#                     continue
#                 if ([x,a] not in connections):
#                     self.ans+=1
#                 self.visited.add(x)
        
#         dfs(0)
#         return self.ans
        changes = 0
        visited = set()
        edges = {(a, b) for a, b in connections}
        neighbour = {a:[] for a in range(n)}

        for a, b in connections:
            neighbour[a].append(b)
            neighbour[b].append(a)
        self.ans = 0


        def dfs(i):
            
            for nei in neighbour[i]:
                if nei in visited:
                    continue
                if (i, nei) in edges:
                    self.ans += 1
                visited.add(i)
                dfs(nei)
        dfs(0)

        return self.ans




        
        
        
        # working_nodes = set()
        # working_nodes.add(0)
        # ans = 0
        # connections.sort(key = lambda x: x[1] )
        # print(connections)
        # for conn in connections:
        #     if conn[1] in working_nodes:
        #         working_nodes.add(conn[1])
        #         working_nodes.add(conn[0])
        #     else:
        #         ans += 1
        #         working_nodes.add(conn[1])
        #         working_nodes.add(conn[0])
        #         # print(conn[1])
        # return ans
        
        
        