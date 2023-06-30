class Solution:
    # def fib(self, n: int) -> int:
    #     pos0 = 0
    #     pos1 = 1
    #     if(n < 2):
    #         return n
    #     for i in range(2,n+1):
    #         pos1, pos0 = pos1 + pos0, pos1
    #     return pos1
    
    ##recursion
    
#     def fib(self, n: int) -> int:
#         def rec(i):
#             if i == 0:
#                 return 0
#             if i == 1:
#                 return 1
            
#             return rec(i - 1) + rec(i-2)
#         return rec(n)
    
    ## recursion with memoization
    
    def fib(self, n: int) -> int:
        memo = {}
        def rec(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            if i in memo:
                return memo[i]
            memo[i] = rec(i - 1) + rec(i-2)
            return memo[i]
        return rec(n)
    
        