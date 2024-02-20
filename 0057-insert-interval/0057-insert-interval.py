class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        result.append(newInterval)
        return result
    
    
    
        result = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)

        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result
    
    
    
    
        #Binary Search
        def binary_search(x, n):
            s = 0
            e = len(x) - 1
            while s<=e:
                mid = (s+e)//2
                if x[mid] == n:
                    return mid
                elif x[mid] < n:
                    s  = mid + 1
                else:
                    e = mid - 1
            return e+1

        if not intervals:
            intervals.append(newInterval)
            return intervals
        x = []
        for i in range(len(intervals)):
            x.append(intervals[i][1])

        k = binary_search(x,newInterval[0])
        res = intervals[:k] #to store intervals till `k`th index
        while k < len(intervals) and intervals[k][0] <= newInterval[1]:
            newInterval[0] = min(intervals[k][0], newInterval[0])
            newInterval[1] = max(intervals[k][1], newInterval[1])
            k += 1
        res.append(newInterval)
        #adding remaining elements to the list
        res += intervals[k:]  
        return res 
    
    
    
