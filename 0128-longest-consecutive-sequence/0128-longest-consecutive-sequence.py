class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for i in nums_set:
            if i-1 not in nums_set:
                leng = 1
                while(i+1 in nums_set):
                    leng +=1
                    i+=1
                ans = max(ans,leng)
        return ans
                
                
        