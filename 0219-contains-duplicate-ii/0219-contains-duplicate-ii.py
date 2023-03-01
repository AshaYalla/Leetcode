class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapp = defaultdict(list)
        for i in range(len(nums)):
            if nums[i] not in mapp:
                mapp[nums[i]] = [i]
            else:
               mapp[nums[i]].append(i)
        for i in mapp:
            for j in range(1,len(mapp[i])):
                if(mapp[i][j] is None):
                    continue
                else:
                    if(abs(mapp[i][j] - mapp[i][j-1]) <= k):
                        return True
        return False
                