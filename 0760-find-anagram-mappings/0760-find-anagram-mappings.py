class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictt = defaultdict(list)
        for i, x in enumerate(nums2):
            dictt[x].append(i)
        return [ dictt[j].pop() for j in nums1]
    