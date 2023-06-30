class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for i in paths:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        color = [0] * (n + 1)
        ans = []
        
        def garden(count, color):
            if( count == n+1):
                ans.extend(color[1:])
                return True
            
            for i in range(1,5):
                proceed = 1
                for j in graph[count]:
                    if color[j] == i:
                        proceed = 0
                if(proceed):
                    color[count] = i
                    if garden(count+1 , color):
                        return True
                    color[count] = 0
            return False
        if garden(1,color):
            return ans
        
                
                
                
        