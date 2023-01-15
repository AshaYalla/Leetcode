#find peak element in the biotonic arrary and search as per the order of the array divided by the peak element. 

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        l,r = 1, mountain_arr.length()-1
        peak = 0
        while(l<=r):
            mid = (l+r) // 2
            if((mountain_arr.get(mid) > mountain_arr.get(mid-1) )and (mountain_arr.get(mid) > mountain_arr.get(mid+1))):
                peak = mid
                break
            elif(mountain_arr.get(mid) < mountain_arr.get(mid+1)):
                l = mid+1
            else:
                r = mid-1
        l,r = 0,peak
        while(l<=r):
            mid = (l+r)//2
            if(mountain_arr.get(mid) == target):
                return mid
            elif(mountain_arr.get(mid) > target):
                r = mid -1
            else:
                l = mid + 1
        l,r = peak,mountain_arr.length()-1
        while(l<=r):
            mid = (l+r)//2
            if(mountain_arr.get(mid) == target):
                return mid
            elif(mountain_arr.get(mid) > target):
                l = mid + 1
                
            else:
                r = mid -1
        return -1
                
            
        
        
        