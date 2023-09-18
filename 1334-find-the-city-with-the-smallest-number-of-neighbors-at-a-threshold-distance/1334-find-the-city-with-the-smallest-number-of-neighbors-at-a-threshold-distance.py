class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        # bellman-ford
        adjList = defaultdict(list)
        for u, v, w  in edges:
            adjList[u].append([v, w])
            adjList[v].append([u, w])
        
        minNeigh, res = float('inf'), 0
        # update each row
        for i in range(n):

            # setup
            dist = [float('inf')] * n
            dist[i] = 0
            q = deque([i])
            
            while q: # update while the distance decreased
                node = q.popleft()

                for nei, w in adjList[node]:
                    if dist[node] + w < dist[nei]:
                        dist[nei] = dist[node] + w
                        q.append(nei)

            neiCnt = 0
            for j in range(n):
                if i != j and dist[j] <= distanceThreshold:
                    neiCnt += 1
            if minNeigh >= neiCnt:
                minNeigh, res = neiCnt, i

        return res




        # Floyd
        dist = [[float('inf')] * n for _ in range(n)]

        # set the base case
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        for i in range(n):
            dist[i][i] = 0
        
        # update each dist
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        res = {sum(d <= distanceThreshold for d in dist[i]): i for i in range(n)}
        return res[min(res)]




        # dikstra's
        # for all vertex pair, get the min distance to travel from u to v
        adjList = defaultdict(list)
        for u, v, w  in edges:
            adjList[u].append([v, w])
            adjList[v].append([u, w])

        # for all vertex count the neighbors that meets the threshold
            # get the max city index that has the min number of neighbors
        res = 0
        minNeigh = float('inf')
        for i in range(n):
            minHeap = [(0, i)]
            visit = set()

            neiCnt = 0
            while minHeap:
                w, node = heapq.heappop(minHeap)

                # stop searching from the node if past threshold
                if node in visit:
                    continue
                
                visit.add(node)
                if node != i: # add to the neighbors
                    neiCnt += 1
                
                for nei, dist in adjList[node]:
                    if nei not in visit and w + dist <= distanceThreshold:
                        heapq.heappush(minHeap, (w + dist, nei))

            # update the global minNeigh
            if neiCnt <= minNeigh:
                res, minNeigh = i, neiCnt

        return res  