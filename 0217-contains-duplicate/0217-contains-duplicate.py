class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictt = collections.defaultdict(bool)
        for i in range(len(nums)):
            if dictt[nums[i]]:
                return True
            dictt[nums[i]] = True
        return False
        