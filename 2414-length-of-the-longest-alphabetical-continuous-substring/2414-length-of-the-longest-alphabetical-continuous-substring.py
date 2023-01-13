class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        maxi = mx = 1
        for i in range(1,len(s)):
            if(ord(s[i]) == ord(s[i-1]) +1 ):
                mx+=1
            else:
                mx = 1
            maxi = max(maxi,mx)
        return maxi
        