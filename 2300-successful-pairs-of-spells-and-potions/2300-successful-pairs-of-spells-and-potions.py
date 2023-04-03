class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        tot = len(potions)
        potions.sort()
        for i in spells:
            l = 0
            r = len(potions)
            
            while(l<r):
                mid = (l+r) // 2
                if(i * potions[mid] >= success):
                    r = mid
                else:
                    l = mid +1
            res.append(tot - l)
        return res
            
        
        