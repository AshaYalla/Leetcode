class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        #slidingwindow
        n = len(arr)
        l, r = 0, 0
        ans = 1
        if n == 1:
            return 1
        while r < n:
            while l < n - 1 and arr[l] == arr[l+1]: # to handle duplicates
                l += 1
            while r < n - 1 and (arr[r-1] > arr[r] < arr[r+1] or arr[r-1] < arr[r] > arr[r+1]):
                r += 1
            ans=max(ans, r - l + 1)
            l = r
            r += 1
        return ans
#         cur, mx, t = 1, 1, None
#         for i in range(1, len(arr)):
#             if t == None:
#                 if arr[i] != arr[i-1]: 
#                     cur = 2
#                     mx = max(mx, cur)
#                     t = arr[i] > arr[i-1]
#             elif (t and arr[i] < arr[i-1]) or (not t and arr[i] > arr[i-1]):
#                 cur += 1; t = not t
#                 mx = max(mx, cur)

#             else:
#                 if arr[i] == arr[i-1]: t = None
#                 cur = 2
        
#         return mx