class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = dict()
        def solve(i,rem):
            if rem < 0:
                return -1
            if i < 0:
                if rem == 0:
                    return 0
                else:
                    return inf
            
            if (i,rem) in dp:
                return dp[(i,rem)]
            
            if coins[i] > rem:
                ans = solve(i-1,rem)
            else:
                ans =  min( solve(i-1,rem),1+ solve(i,rem - coins[i]))
            dp[(i,rem)] = ans
            return ans
        ans = solve(n-1,amount)
        if ans == inf:
            return -1
        else:
            return ans

        