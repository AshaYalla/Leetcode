class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        a,a1= len(word1)-1,len(word1)-1
        b,b1 = len(word2)-1,len(word2)-1
        while(a >= 0 and b >=0):
            res.append(word1[a1-a])
            res.append(word2[b1-b])
            a-=1
            b-=1
        while(a >=0):
            res.append(word1[a1-a])
            a-=1
        while(b >=0):
            res.append(word2[b1-b])
            b-=1
        return "".join(res)
            
                

        
        
        