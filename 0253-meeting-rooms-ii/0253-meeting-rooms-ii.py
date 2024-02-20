class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starttime = [i[0] for i in intervals]
        starttime.sort()

        endtime = [i[1] for i in intervals]
        endtime.sort()
        count = 0
        k = 0
        ans = 0
        i = 0

        while i < len(intervals):
            if( starttime[i] < endtime[k]):
                count+=1
                i+=1
            else:
                count-=1
                k+=1
            ans = max(count,ans)
        return ans
            
                
            
            
        