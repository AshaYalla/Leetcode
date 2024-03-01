class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        firstdict = defaultdict(list)
        secdict = defaultdict(list)
        
        for idx, [i,j] in enumerate(stones):
            firstdict[i].append(idx)
            secdict[j].append(idx)
            
        self.visited = set()
        
        def dfs(i):
            if i in self.visited:
                return 
            self.visited.add(i)
            r,c = stones[i]
            
            for x in firstdict[r]:
                if x in self.visited:
                    continue
                dfs(x)
            for y in secdict[c]:
                if y in self.visited:
                    continue
                dfs(y)
            
        ans = 0   
            
        for i in range(len(stones)):
            if i in self.visited:
                continue
            ans+=1
            dfs(i)
        return len(stones) - ans
            
        