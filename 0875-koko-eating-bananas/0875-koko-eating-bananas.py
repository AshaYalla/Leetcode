class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        
        while(l<r):
            mid = (l+r) // 2
            
            hours = 0
            for i in piles:
                hours += math.ceil(i/mid)
            if hours > h:
                l = mid + 1
                
            else:
                r = mid
                
                
        return l
                
        l = min(piles)
        r = max(piles)
        
        while(l <r):
            mid = l + r // 2
            hoursreq = 0
            for i in piles:
                hoursreq += i // mid
                if i % mid:
                    hoursreq+=1
            
            if hoursreq <= h:
                r = mid
                
            else:
                l = mid + 1
                
        return l
                  