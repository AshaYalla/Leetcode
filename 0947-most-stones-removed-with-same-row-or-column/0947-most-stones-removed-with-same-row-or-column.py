class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        rank = [1] * n
        parent = [i for i in range(n)]
        
        def union(i, j):
            i, j = find(i), find(j)
            if i == j:
                return 0
            if rank[i] < rank[j]:
                i, j = j, i
            rank[i] += rank[j]
            parent[j] = parent[i]
            return 1
        
        def find(i):
            while i != parent[i]:
                parent[i] = i = parent[parent[i]]
            return i
        
        rows, cols = {}, {}
        removed = 0
        for i, (row, col) in enumerate(stones):
            if row in rows:
                removed += union(i, rows[row])
            else:
                rows[row] = i
            if col in cols:
                removed += union(i, cols[col])
            else:
                cols[col] = i
        
        return removed
# class Solution:
#     def removeStones(self, stones: List[List[int]]) -> int:
#         firstdict = defaultdict(list)
#         secdict = defaultdict(list)
        
#         for idx, [i,j] in enumerate(stones):
#             firstdict[i].append(idx)
#             secdict[j].append(idx)
            
#         self.visited = set()
        
#         def dfs(i):
#             if i in self.visited:
#                 return 
#             self.visited.add(i)
#             r,c = stones[i]
            
#             for x in firstdict[r]:
#                 if x in self.visited:
#                     continue
#                 dfs(x)
#             for y in secdict[c]:
#                 if y in self.visited:
#                     continue
#                 dfs(y)
            
#         ans = 0   
            
#         for i in range(len(stones)):
#             if i in self.visited:
#                 continue
#             ans+=1
#             dfs(i)
#         return len(stones) - ans
            
        