class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def solve(ind,target):
            if target==0:
                ans.append(op[:])
                return 
            for i in range(ind,len(candidates)):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                op.append(candidates[i])
                solve(i+1,target-candidates[i])
                op.pop()
        candidates.sort()
        ans=[]
        op=[]
        solve(0,target)
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if target %2 != 0:
        #     return 0
        # ans = []
        # candidates.sort()
        # dp = dict()
        # def combi(tar, comb, start):
        #     if tar == 0:
        #         if comb not in ans:
        #             ans.append(list(comb))
        #         return
        #     if start == len(candidates):
        #         return
        #     elif tar < 0:
        #         return 
        #     if (tar, comb, start) in dp:
        #         return dp[(tar, comb, start)]
        #     comb.append(candidates[start])
        #     combi(tar - candidates[start],comb,start+1)
        #     comb.pop()
        #     combi(tar,comb,start+1)
        # combi(target,[],0)
        # return ans