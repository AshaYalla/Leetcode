class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r = len(image)
        c = len(image[0])
        
        nei = [(1,0),(0,1),(-1,0),(0,-1)]
        queue = []
        visited = set()
    
        col = image[sr][sc] 
        queue.append((sr,sc))
        visited.add((sr,sc))
        image[sr][sc] = color

        while(queue):
            ni,nj = queue.pop()

            for i,j in nei:
                if (ni+i, nj+j) not in visited and ni+i >= 0 and ni+i < r and nj+j >= 0 and nj+j < c and image[ni+i][nj+j] == col:
                    image[ni+i][nj+j] = color
                    queue.append((ni+i, nj+j))
                    visited.add((ni+i, nj+j))
        return image
        