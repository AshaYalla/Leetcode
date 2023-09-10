class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * (numCourses)
        graph = defaultdict(list)
        for i,j in prerequisites:
            indegree[i] +=1
            graph[j].append(i)
        q = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        res = []   
        while(q):
            i = q.pop(0)
            res.append(i)
            for nei in graph[i]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(res) == numCourses:
            return res
        else:
            return []
    

                
                
            
        