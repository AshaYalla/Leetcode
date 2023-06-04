class Solution:
    def __init__(self):
        self.cities_visited = set()

    def bfs(self, city, cities_graph):
        self.cities_visited.add(city)
        queue = [city]
        while queue:
            c = queue.pop(0)
            for i in cities_graph[c]:
                if i not in self.cities_visited:
                    self.cities_visited.add(i)
                    queue.append(i)

    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        rows, cols = len(isConnected), len(isConnected[0])

        cities_graph = [[] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i != j and isConnected[i][j] == 1:
                    cities_graph[i].append(j)

        provinces = 0

        for city in range(rows):
            if city not in self.cities_visited:
                self.bfs(city, cities_graph)
                provinces += 1

        return provinces