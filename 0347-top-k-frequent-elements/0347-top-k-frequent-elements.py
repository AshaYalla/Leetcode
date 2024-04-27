class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt = Counter(nums)
        heap = []
        for key,v in dictt.items():
            heapq.heappush(heap,(-v, key))
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
            
        
            
            
        
            
    #s- o(n) ; t- o(nlogn)
            
            
            

            