class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sett = set()
        for i in range(len(nums)):
            print(i)
            
            if nums[i] in sett:
                return True
            sett.add(nums[i])
            if len(sett) > k:
                sett.remove(nums[i-k])
                
        return False

        # if(len(nums) == len(set(nums))):
        #     return False
        # for i in range(0,len(nums)):
        #     for j in range(i+1, min(i+k+1,len(nums))):
        #         if(nums[i] == nums[j] ):
        #             return True
        # return False