class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while(len(stones) > 1):
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            res = a - b
            if res:
                heapq.heappush(stones,res)
            
        return -stones[0] if stones else 0
        