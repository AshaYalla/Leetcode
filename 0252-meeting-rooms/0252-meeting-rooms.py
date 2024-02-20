class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x: x[1])
        maxx = -inf
        
        for i,j in intervals:
            if i >= maxx:
                maxx = j
            else:
                return False
        return True
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if(len(intervals) == 0 or len(intervals) == 1 ):
#             return True
#         ans = sorted(intervals, key = lambda x: x[1])

#         for i in range(0,len(intervals)-1):
#             if(ans[i][1] > ans[i+1][0]):
#                 return False
#         return True