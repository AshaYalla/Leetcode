class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dictt = {}
        
        def summ(i,rem):
            if i == n: 
                if rem == target:
                    return 1
                else:
                    return 0 
            if (i,rem) in dictt:
                return dictt[(i,rem)]
            c1 = summ(i+1,rem + nums[i])
            c2 = summ(i+1,rem - nums[i])
            c = c1 + c2
            dictt[(i, rem)] = c
            return c1+ c2
            
        return summ(0,0)
    

        