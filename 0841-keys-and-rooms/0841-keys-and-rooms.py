class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in range(len(rooms)):
            graph[i] += (rooms[i])
            
        queue = graph[0]
        visited = set()
        visited.add(0)
        
        while(queue):
            i = queue.pop(0)
            visited.add(i)
            for child in graph[i]:
                if child not in visited:
                    queue.append(child)
                    
        print(visited, graph)
        return(len(visited) == len(graph))
            
            
            
        