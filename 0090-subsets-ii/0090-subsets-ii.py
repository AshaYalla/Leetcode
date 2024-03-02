class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        def sub(i,summ ):
            if(i == n):
                if summ not in ans:
                    ans.append(list(summ))
                return
            
            for j in range(i,n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                summ.append(nums[j])
                sub(j+1,summ )
                summ.pop()  
                sub(j+1,summ )
                
        sub(0,[])
        ans.sort()
        return ans
            
        

