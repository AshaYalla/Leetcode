class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = defaultdict(int)
        
        for i,x in enumerate(nums):
            if target -x in dictt:
                return [i,dictt[target -x]]
            dictt[x] = i
        
