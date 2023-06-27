class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def combi(tar, comb, start):
            if tar == 0:
                if comb not in ans:
                    ans.append(list(comb))
                return
            elif tar < 0:
                return 
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                comb.append(candidates[i])
                combi(tar - candidates[i],comb,i+1)
                comb.pop()
        combi(target,[],0)
        return ans