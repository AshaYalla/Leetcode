class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        ans = []
        nums.sort()
        use = [0] * n
        
        def permute(comb, use, i):
            if i == n:
                ans.append(comb[:])
            for j in range(n):
                if not use[j]:
                    comb.append(nums[j])
                    use[j] = 1
                    permute(comb,use,i+1)
                    use[j] = 0
                    comb.pop()

        permute([],use,0)
        return ans
                
        