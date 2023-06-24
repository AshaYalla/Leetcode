class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates) - 1
        
        def combi(i,target,arr):
            if(i == n):
                if(target == 0):
                    ans.append(arr)
                return
            if candidates[i] <= target:
                arr.append(candidates[i])
                combi(i,target-candidates[i],arr)
                arr.pop()
            combi(i+1,target,arr)
        combi(0,target,[])
        return ans
    
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def findcombination(i,target,li,ans):
            if i==len(candidates): # Base Condition
                if target==0 and li not in ans:
                    ans.append(li.copy())
                return     
            if candidates[i]<=target:
                li.append(candidates[i])
                findcombination(i,target-candidates[i],li,ans)
                li.pop()
            findcombination(i+1,target,li,ans)
            return ans
            
        return findcombination(0,target,li=[],ans=[]) 
            