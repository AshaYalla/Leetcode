class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while(l < r):
            mid = (l+r) // 2
            summ = 0
            k = 1
            for i in weights:
                summ+=i
                if(summ > mid):
                    summ = i
                    k+=1
            if k <= days:
                r = mid
            else:
                l = mid + 1
        return l
         
                
        