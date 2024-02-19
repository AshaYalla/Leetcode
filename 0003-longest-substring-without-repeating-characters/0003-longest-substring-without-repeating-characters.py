class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        mp = {}

        i = 0
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        start = 0
        maxx = 0
        for i in range(len(s)):
            while s[i] in sett:
                sett.remove(s[start])
                start+=1
            sett.add(s[i])
            if(len(sett) == i-start+1):
                maxx = max(maxx,i-start+1)
        return maxx
        