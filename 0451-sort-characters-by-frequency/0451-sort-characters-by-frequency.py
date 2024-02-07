class Solution:
    def frequencySort(self, s: str) -> str:
        dictt = Counter(s)
        ans = ""
    
        for i in sorted(dictt.items(), key=lambda x:x[1], reverse=True ):
        
            ans+=i[0]*i[1]
        return ans
            
        