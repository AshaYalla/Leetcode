class Solution:
    def climbStairs(self, n: int) -> int:
        dictt = {}
        def solve(i):
            if i == 0:
                return 1
            if i < 0:
                return 0 
            if i in dictt:
                return dictt[i]
            c1 = solve(i-2)
            c2 = solve(i-1)
            dictt[i] = c1+c2
            return c1+c2
        return solve(n)
        
            
        