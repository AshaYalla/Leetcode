class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        cur, mx, t = 1, 1, None
        for i in range(1, len(arr)):
            # Start of subarray
            if t == None:
                if arr[i] != arr[i-1]: 
                    cur = 2
                    t = arr[i] > arr[i-1]
            # Valid element in subarray, continue cur subarray
            elif (t and arr[i] < arr[i-1]) or (not t and arr[i] > arr[i-1]):
                cur += 1; t = not t
            # Invalid element in subarray, start new subarray
            else:
                if arr[i] == arr[i-1]: t = None
                mx = max(mx, cur)
                cur = 2
        
        return max(mx, cur)
#         if len(arr) == 1 or len(arr) == 2 :
#             return  len(arr)
#         l = 0
#         maxx = 2
#         r = 0
#         prev = arr[0] > arr[1]
        
#         if arr[0] == arr[1]:
#             l = 1
        
        
#         for i in range(1, len(arr) - 1):
                
#             if arr[i] == arr[i+1]:
#                 maxx = max(maxx,1)
#                 l = i+1
#                 continue
            
#             if (prev and arr[i] < arr[i+1]) or ((not prev) and arr[i] > arr[i+1]):
#                 r = i+1
#                 print(r-l+1)
#                 maxx = max(r-l+1, maxx)
                
#             else:
#                 l = i
            
#             prev = arr[i] > arr[i+1]
#         return maxx
                
            
            

                
        