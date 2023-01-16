class Solution:
    def minDays(self, A: List[int], m: int, k: int) -> int:
        def isFeasible(x):
            aj_flw = count_flw =0
            
            for i in A:
                if x>=i:
                    aj_flw += 1
                else:
                    aj_flw = 0
                if aj_flw == k:
                    count_flw += 1 
                    aj_flw = 0
            return count_flw >=m
                    
        if len(A)<m*k: return -1 
        l,r = 1,max(A) 
        
        while l<=r:
            mid = l+(r-l)//2 
            if isFeasible(mid):
                r = mid - 1 
            else:
                l = mid + 1
                 
        return l
                    
        