class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def combi(tar, comb, start):
            if tar == 0:
                ans.append(list(comb))
                return
            elif tar < 0:
                return 
            for i in range(start,len(candidates)):
                comb.append(candidates[i])
                combi(tar - candidates[i],comb,i)
                comb.pop()
        combi(target,[],0)
        return ans
            