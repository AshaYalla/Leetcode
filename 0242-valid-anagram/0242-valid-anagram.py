class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        buffer = [0]*26
        for i in range(len(s)):
            buffer[ord(s[i]) - ord('a')] +=1
            buffer[ord(t[i]) - ord('a')] -=1
        for i in buffer:
            if i:
                return False
        return True
            

    
    
    #timecomplexity - O(n)
    #spacecomplexity - O(26) - O(1)
        