class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = Counter(nums)

        arr = []
        for key,value in dict.items():
            arr.append((-value,key))
        heapq.heapify(arr)
        result = []
        for i in range(k):
            result.append(heapq.heappop(arr)[1])
        return result
    
    #s- o(n) ; t- o(nlogn)
            
            
            

            