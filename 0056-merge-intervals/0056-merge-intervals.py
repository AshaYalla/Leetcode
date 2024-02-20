class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x : x[0])
        print(intervals)
        ans = []
        start,end = intervals[0][0],intervals[0][1]
        for i in range(1,len(intervals)):
            if(intervals[i][0] > end):
                ans.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
            elif(intervals[i][0] <= end and intervals[i][1] > end):
                end = intervals[i][1]
        ans.append([start,end])
        return(ans) 
                
        