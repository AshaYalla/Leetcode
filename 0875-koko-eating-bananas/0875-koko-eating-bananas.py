class Solution:
    def minEatingSpeed(self,piles: List[int], H: int) -> int:   
        l = 1
        r = max(piles)
        while(l < r):
            mid = l + (r - l) // 2
            count = 0
            for i in piles:
                count += math.ceil(i/mid) 
            if count<=H:
                r = mid
            else:
                l = mid + 1
        return l
        