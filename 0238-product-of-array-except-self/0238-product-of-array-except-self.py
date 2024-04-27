class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        
        for i in range(1,len(nums)):
            ans[i] = ans[i-1] *nums[i-1]
        
        prev = 1
        for i in range(len(nums)-2,-1,-1):
            prev = prev * nums[i+1]
            ans[i] = ans[i] * prev
            
        
        return ans

# intution: consider [1, 1,2,3, 3] Product of Array Except Self for 2 is nothing but produt of left and rightside
# so, consider a ans with all 1's . start multiplication from left side, multiply prev element and prev product value until prev; update this to current index. 
# do the same for right side; but the ans array already has left elements product so a prev variable should be maintained 
