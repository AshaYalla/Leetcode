class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        dictt = {}
        maxx = 0
        while(r <= len(s) -1):
            if(s[r] in dictt):
                dictt[s[r]]+=1
            else:
                dictt[s[r]]=1
            while(r-l+1-max(dictt.values()) > k):
                dictt[s[l]]-=1
                l+=1
            maxx = max(maxx,r-l+1)
            r=r+1
        return maxx


            
            
            
                    
                
            
                
            
            
        