class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        dictt = defaultdict(int)
        l =0
        maxx = 0
        for r in range(len(s)):
            dictt[s[r]]+=1
            cur = r - l+1 - max(dictt.values())
            if cur <=k:
                maxx = max(r-l+1,maxx)
            else:
                dictt[s[l]]-=1
                if dictt[s[l]] == 0:
                    dictt.pop(s[l])
                l+=1
            
        return maxx
            
            
            
                    
                
            
                
            
            
        