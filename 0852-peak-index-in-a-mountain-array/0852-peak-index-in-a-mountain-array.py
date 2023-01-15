class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r = 0, len(arr)-1
        peak = 0
        while(l<=r):
            mid = (l+r) // 2
            if((arr[mid] > arr[mid-1] )and (arr[mid] > arr[mid+1])):
                peak = mid
                break
            elif(arr[mid] < arr[mid+1]):
                l = mid+1
            else:
                r = mid-1
        return peak
        