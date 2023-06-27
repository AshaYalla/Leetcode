class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def sub(i,summ ):
            if(i == n):
                ans.append(list(summ))
                return
            
            summ.append(nums[i])
            sub(i+1,summ )
            summ.pop()
            sub(i+1, summ)
            
        sub(0,[])
        ans.sort()
        return ans
            
        