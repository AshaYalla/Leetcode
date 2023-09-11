class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for i in words:
            for j in i:
                graph[j] = []
                indegree[j] = 0
                
        for i in range(len(words) -1 ):
            a = words[i]
            b = words[i+1]
            minn = min(len(a)-1, len(b)-1)
            
            if len(a) > len(b) and a[:minn+1] == b[:minn+1]:
                print("meh")
                return ""
            j = 0
            while j <= (minn):
                if a[j] == b[j]:
                    j+=1
                else:
                    indegree[a[j]] +=1
                    graph[b[j]].append(a[j])
                    break
        q = [] 
        ans = []
        visited = set()
        for i in indegree:
            if indegree[i] == 0:
                q.append(i)

        
        while(q):
            node = q.pop(0)
            ans.append(node)
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
                    
        print(ans,graph)
        print(len(ans))
        print(len(indegree))
  
        if len(ans) != len(indegree):
            return ""
        else:
            return "".join(ans[::-1])
                    


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         graph = defaultdict(list)
#         indegree = defaultdict(int)
#         for i in words:
#             for j in i:
#                 graph[j] = []
#                 indegree[j] = 0
                
#         for i in range(len(words)-1):
#             l = min(len(words[i]), len(words[i+1]))
#             a,b = words[i], words[i+1]
#             if len(a) > len(b) and a[:l] == b[:l]:
#                 return ""
#             for j in range(min(len(a),len(b))):
#                 if words[i][j] != words[i+1][j]:
#                     graph[words[i][j]].append(words[i+1][j]) 
#                     indegree[words[i+1][j]]+=1
#                     break
#         visited = []
#         queue = [i for i in indegree if indegree[i] == 0]
#         if queue == []: 
#             return ""
#         while queue:
#             temp = queue.pop(0)
#             visited.append(temp)
#             for i in graph[temp]:
#                 if i not in visited:
#                     indegree[i]-=1
#                 if indegree[i] == 0:
#                     queue.append(i) 
#         if len(visited) == len(indegree):
#             return("".join(visited))
#         else:
#             return ""
                           
                           