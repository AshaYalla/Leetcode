class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key = lambda x : x[2])
        time = collections.defaultdict(list)
        for i in meetings:
            time[i[2]].append([i[0],i[1]])

        secret = {0, firstPerson}
        for timed, meeting in time.items():
 
            graph = collections.defaultdict(list)
            seen = set()
            for i in meeting:
                graph[i[0]].append(i[1]) 
                graph[i[1]].append(i[0])
                if(i[0] in secret):
                    seen.add(i[0])
                if(i[1] in secret):
                    seen.add(i[1])

            while(seen):
                cur = seen.pop()
                for i in graph[cur]:
                    if i not in secret:
                        secret.add(i)
                        seen.add(i)
                    
        return secret
            
                
            
                    

                
            
            