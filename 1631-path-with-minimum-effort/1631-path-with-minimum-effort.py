class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r = len(heights)
        c = len(heights[0])
        
        dis = [[float(inf) for i in range(len(heights[0]))] for j in range(len(heights))]
        vis = [[False for i in range(len(heights[0]))] for j in range(len(heights))]
        
        dis[0][0] = 0
        
        q = [(0,0,0)]
        nei = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while(q):
            d,x,y = heapq.heappop(q)
            vis[x][y] = True
            for nx,ny in nei:
                if x+nx >= 0 and x+nx < r and y+ny >= 0 and y+ny < c and not vis[x+nx][y+ny]:
                    diff = abs(heights[x+nx][y+ny] - heights[x][y])
                    maxdiff = max(diff,dis[x][y])
                    if dis[x+nx][y+ny] > maxdiff:
                        dis[x+nx][y+ny]  = maxdiff
                        heapq.heappush(
                            q,(maxdiff, x+nx,y+ny))
        return dis[-1][-1]

        