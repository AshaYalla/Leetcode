class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        use = [0] * n
        
        def permute(comb, use):
            if len(comb) == n:
                ans.append(comb[:])
                return
            for num in use:
                if use[num] > 0:
                    comb.append(num)
                    use[num] -= 1
                    permute(comb, use)
                    comb.pop()
                    use[num] += 1

        permute([],Counter(nums))
        return ans
                