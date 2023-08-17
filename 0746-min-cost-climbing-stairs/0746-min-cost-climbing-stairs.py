class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def solve(i):
            if i <= 1:
                return 0
            return min(cost[i-1] + solve(i-1), cost[i-2] + solve(i-2))
        return solve(len(cost))
            
        