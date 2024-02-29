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
            


                

                
            
    
            
        