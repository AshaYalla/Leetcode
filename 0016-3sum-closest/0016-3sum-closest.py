class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = inf
        for i in range(len(nums)):
            lo, hi = i+1, len(nums) -1
            while lo < hi:
                summ = nums[i]+nums[lo]+nums[hi]
                if abs(target-summ) < abs(diff):
                    diff = target -summ
                if summ < target:
                    lo+=1
                else:
                    hi-=1
        return target - diff
            