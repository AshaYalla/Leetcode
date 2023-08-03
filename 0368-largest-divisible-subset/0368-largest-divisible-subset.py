class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        dp = [0] * len(nums)
        
        temp = [i for i in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        temp[i] = j
                        dp[i] = dp[j] + 1
                        
        print("dp",dp)
        print("temp",temp)
        ans = []
                    
        mval, mind = max([(v, i) for i, v in enumerate(dp)])
        ans.append(nums[mind])
        
        while(mind != temp[mind]):
            mind = temp[mind]
            ans.append(nums[mind])
            
        return ans[::-1]
        
        
        
                
                

        
        
                    
        
        