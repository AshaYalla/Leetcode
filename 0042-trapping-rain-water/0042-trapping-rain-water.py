class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) -1 
        ans = 0
        leftmax, rightmax = height[l], height[r]
        while(l<r):
            if height[l] < height[r]:
                l+=1
                leftmax = max(height[l], leftmax)
                ans += leftmax - height[l]
            else:
                r-=1
                rightmax = max(height[r], rightmax)
                ans += rightmax - height[r]
        return ans
                
        