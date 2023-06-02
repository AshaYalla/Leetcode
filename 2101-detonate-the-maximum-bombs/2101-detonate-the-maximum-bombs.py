class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue
                if bombs[i][2] >= math.sqrt((bombs[i][1] - bombs[j][1])**2 + (bombs[i][0] - bombs[j][0])**2):
                    graph[i].append(j)
                    
        def bfs(i):
            queue = collections.deque([i])
            visited = set([i])
            while queue:
                cur = queue.popleft()
                for neib in graph[cur]:
                    if neib not in visited:
                        visited.add(neib)
                        queue.append(neib)
            return len(visited)

        answer = 0
        for i in range(len(bombs)):
            answer = max(answer, bfs(i))

        return answer