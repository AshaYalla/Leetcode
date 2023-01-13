class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset = set(nums)
        answer = 0
        for i in numsset:
            if(i-1 not in numsset):
                answer1 = 1
                while i + 1  in numsset:
                    answer1 += 1
                    i = i+1
                answer = max(answer1, answer)
        return answer

                
        