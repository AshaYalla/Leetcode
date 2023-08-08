class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}
        for i,v in enumerate(nums):
            if target - v in dictt:
                j = dictt[target-v]
                return [i,j]
            dictt[v] = i
        