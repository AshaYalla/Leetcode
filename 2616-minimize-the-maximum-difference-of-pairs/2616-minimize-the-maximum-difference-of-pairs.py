class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        
        def paircount(t):
            count = 0
            i = 0
            while i < (len(nums)-1):
                if nums[i+1] - nums[i]  <= t:
                    count+=1
                    i+=1
                i+=1
            return count
        
        l,r = 0,nums[-1] - nums[0]
        while(l<r):
            mid = (l + r) // 2
            if paircount(mid) >= p:
                r = mid
            else:
                l = mid + 1
        return l
                    
        