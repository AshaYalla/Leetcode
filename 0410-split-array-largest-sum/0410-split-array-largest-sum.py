class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # left, right = max(nums), sum(nums)
        # while left < right:
        #     mid = left + (right - left) // 2
        #     count = 1
        #     total = 0
        #     for num in nums:
        #         total += num
        #         if total > mid:
        #             total = num
        #             count += 1
        #     if count <= k:
        #         right = mid     
        #     else:
        #         left = mid + 1
        # return left
        l = max(nums)
        r = sum(nums)
        while(l<r):
            summ = 0
            count = 1
            
            mid = (l+r) // 2
            for i in nums:
                summ+=i
                if(summ > mid):
                    summ = i
                    count+=1
            if(count <=k):
                r = mid
            else:
                l = mid +1
        return l
                