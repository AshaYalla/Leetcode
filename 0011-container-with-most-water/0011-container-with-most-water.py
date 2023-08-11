class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height ) - 1
        ans = 0
        while(l<r):
            w = r - l
            area = w * min(height[l], height[r])
            ans = max(ans,area)
            if(height[l] < height[r]):
                l = l+1
            else:
                r = r-1
            
        return ans
            