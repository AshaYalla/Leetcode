class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictt = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in dictt:
                l = max(l,dictt[s[r]]+1)
            dictt[s[r]] = r
            res = max(res, r-l+1)
        return res
                
                