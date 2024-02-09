class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        high = { x: i for i,x in enumerate(s)}
        
        maxx = 0
        ans = []
        prev = -1
        
        for i in range(len(s)):
            maxx = max( maxx, high[s[i]])
            if i == maxx:
                ans.append(maxx - prev )
                prev = maxx
                
        return ans
                
                

                        
                
                