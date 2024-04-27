class Solution:
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
        dict = {}
        res = 0
        
        l = 0
        for r in range(len(s)):
            if s[r] in dict:
                l = max(l, dict[s[r]] + 1)
            res = max(res, r-l+1)
            dict[s[r]] = r
            
        return res

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     sett = set()
    #     start = 0
    #     maxx = 0
    #     for i in range(len(s)):
    #         while s[i] in sett:
    #             sett.remove(s[start])
    #             start+=1
    #         sett.add(s[i])
    #         if(len(sett) == i-start+1):
    #             maxx = max(maxx,i-start+1)
    #     return maxx
        