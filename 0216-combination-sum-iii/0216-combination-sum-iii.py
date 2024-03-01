class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        
        def solve(i,path,summ):
            if len(path) == k:
                if summ == n:
                    ans.append(path[:])
                return
            if summ > n:
                return
            for j in range(i,10):
                path.append(j)
                solve(j+1,path,summ+j)
                path.pop()
        solve(1,[],0)
        return ans
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # ans = []
        # def combi(tar, comb, start):
        #     if tar == 0:
        #         if comb not in ans and len(comb) == k:
        #             ans.append(list(comb))
        #         return
        #     elif tar < 0:
        #         return 
        #     for i in range(start,10):
        #         comb.append(i)
        #         combi(tar - i,comb,i+1)
        #         comb.pop()
        # combi(n,[],1)
        # return ans