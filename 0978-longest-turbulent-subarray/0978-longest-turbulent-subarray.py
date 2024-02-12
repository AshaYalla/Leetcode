class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        cur, mx, t = 1, 1, None
        for i in range(1, len(arr)):
            if t == None:
                if arr[i] != arr[i-1]: 
                    cur = 2
                    mx = max(mx, cur)
                    t = arr[i] > arr[i-1]
            elif (t and arr[i] < arr[i-1]) or (not t and arr[i] > arr[i-1]):
                cur += 1; t = not t
                mx = max(mx, cur)

            else:
                if arr[i] == arr[i-1]: t = None
                cur = 2
        
        return mx