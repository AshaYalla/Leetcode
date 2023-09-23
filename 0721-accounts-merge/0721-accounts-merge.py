class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = [i for i in range(n)]
        rank = [0 for i in range(n)]
        def findp(x):
            if x!=parent[x]:
                parent[x] = findp(parent[x])
            return parent[x]
        
        
        for i in range(n):
            for j in range(i+1,n):
                if accounts[i][0] == accounts[j][0]:
                    for k in range(1,len(accounts[j])):
                        if accounts[j][k] in accounts[i]:
                            pi = findp(i)
                            pj = findp(j)
                            if pi == pj:
                                rank[pi]+=1
                                parent[pj] = pi
                            elif rank[pi] > rank[pj]:
                                parent[pj] = pi
                            else:
                                parent[pi] = pj
    
                            
        for i in range(n):
            if i != parent[i]:
                accounts[findp(i)].extend(accounts[i][1:])
        res = []
        for i in range(n):
            if i == parent[i]:
                res.append([accounts[i][0]] + sorted(set(accounts[i][1:])))
            
        return res
            
    
            
        