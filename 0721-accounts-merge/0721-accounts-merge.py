class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = [i for i in range(n)]
        rank = [0 for i in range(n)]
        
        def findp(x):
            while(parent[x]!=x):
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(i,j):
            parent[findp(i)] = findp(j)
            
            
        owner = dict()
        
        
        for i, (_o, *mails) in enumerate(accounts):
            for mail in mails:
                if mail in owner:
                    union(owner[mail], i)
                owner[mail] = i
            
        mergeacc = defaultdict(list)
        for i in owner:
            par = findp(owner[i])
            mergeacc[par].append(i)
        res = []
            
        for i,j in mergeacc.items():
            res.append([accounts[i][0]]+sorted(j))
        return res
            
        
        
    #DFS 
    class Solution:
        def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:        

            em_to_name = {}
            em_graph = defaultdict(set)

            for acc in accounts:
                name = acc[0]

                # making a graph of common connected gmail
                # all acc the gamil start with 1 index
                for email in acc[1:]:

                    # connect 1st to 2nd email
                    em_graph[acc[1]].add(email)

                    #connect 2nd to 1st email
                    em_graph[email].add(acc[1])

                    # create a hashmap
                    # it help us to find the email owners
                    em_to_name[email] = name

            # print(em_graph)
            # print(em_to_name)

            seen = set()
            ans = []

            # dfs function
            def dfs(s,comp):
                if s in seen:
                    return
                seen.add(s)
                comp.append(s)
                for nei in em_graph[s]:
                    if nei not in seen:
                        dfs(nei,comp)    
                return comp  

            # here we use loop to traverse all unconnected
            # components of the graph
            for email in em_graph:
                if email not in seen:
                    component = []
                    dfs(email, component)
                    ans.append([em_to_name[email]] + sorted(component))

            return ans      



                

                
            
    
            
        