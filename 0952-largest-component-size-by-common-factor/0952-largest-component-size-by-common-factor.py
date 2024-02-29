class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        parent = [i for i in range(len(nums))]
        rank = defaultdict(lambda:0)
        
        def findp(x):
            while(x!=parent[x]):
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(idx1, idx2):
            par1,par2 = findp(idx1),findp(idx2)
            if par1!=par2:
                if rank[par1] > rank[par2]:
                    parent[par2] = par1
                elif rank[par2] > rank[par1]:
                    parent[par1] = par2
                else:
                    parent[par2] = par1
                    rank[par1] += 1
        
        factor_parents = defaultdict(int)
    
        
        for i,num in enumerate(nums):
            limit = int(nums[i]**0.5)
            for j in range(2, limit+1):
                if num % j == 0:
                    fac = num//j

                    if fac in factor_parents:
                        union(factor_parents[fac] , i)
                    else:
                        factor_parents[fac] = i
                    if j in factor_parents:
                        union(factor_parents[j] , i)
                    else:
                        factor_parents[j] = i
            if num in factor_parents:
                union(factor_parents[num], i)
            else:
                factor_parents[num] = findp(i)
            

        
        childcount = defaultdict(int)
        maxx = -1
        for i in range(len(nums)):
            par = findp(i)
            childcount[par]+=1
            if childcount[par] > maxx:
                maxx = childcount[par]
        print(parent)
        return maxx
            
            
            
            
            
            
        