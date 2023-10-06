class Solution:
    def integerBreak(self, n: int) -> int:
        dictt = {1:1}
        def dfs(num):
            if num in dictt:
                return dictt[num]
            dictt[num] = 0 if num == n else num
            for i in range(1,num):
                curr = dfs(i) * dfs(num-i)
                dictt[num] = max(dictt[num], curr)
            return dictt[num]
        return dfs(n)
        
                
            