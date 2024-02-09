class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        cur = 0
        ans = 0
        
        for i in range(len(gas)):
            total+=gas[i] - cost[i]
            cur+=gas[i] - cost[i]
            
            if cur < 0:
                cur = 0
                ans = i+1
        if total >= 0:
            return ans
        return -1 
                
            
                
            
            
        
        