def cutRod(price, n):

    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j < i:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], price[i-1] + dp[i][j-i])
    return dp[-1][-1]      


    dp = {}
    def solve(i,rem):
        if (i,rem) in dp:
            return dp[(i,rem)]
        if i < 0:
            if rem == 0:
                return 0
            else:
                return float("-inf")
            
        if rem < 0:
            return float("-inf")
        if i+1 <= rem:
            ans = max(solve(i-1,rem),price[i] + solve(i,rem - i-1))
        else:
            ans = solve(i-1,rem)
        dp[(i,rem)] = ans
        return ans

    return solve(n-1,n)
