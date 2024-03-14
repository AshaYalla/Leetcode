# https://leetcode.com/problems/plates-between-candles/discuss/1549015/Python3-binary-search-and-O(N)-approach
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candies = [i for i, c in enumerate(s) if c == "|"]
        print(candies)
        
        def bns(x: int) -> int:
            l, r = 0, len(candies) - 1
            while l <= r:
                m = (l + r) // 2
                if candies[m] < x: 
                    l = m + 1
                else: 
                    r = m - 1
            return l

        ans = []
        for a, b in queries:
            l, r = bns(a), bns(b + 1) - 1
            ans.append(candies[r] - candies[l] - (r - l) if l < r else 0)
        return ans