class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if(len(bloomDay) < m*k):
            return -1
        l = min(bloomDay)
        r = max(bloomDay)
        while(l<r):
            mid = (l+r) // 2
            maxx = 0
            count = 0
            bq = 0
            for i in bloomDay:
                if i <= mid:
                    count+=1
                else:
                    count = 0   
                if (count == k):
                    bq +=1
                    count = 0
            
            if bq >= m:
                r = mid
            else:
                l = mid +1 
        return l
        
                    
        