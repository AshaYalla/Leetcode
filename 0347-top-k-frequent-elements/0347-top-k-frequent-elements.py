class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] +=1
            else:
                dict[i] = 1
        arr = []
        for key,value in dict.items():
            arr.append((-value,key))
        heapq.heapify(arr)
        result = []
        for i in range(k):
            result.append(heapq.heappop(arr)[1])
        return result
            
            
            

            