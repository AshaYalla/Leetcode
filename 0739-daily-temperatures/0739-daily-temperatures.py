class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0 ] * n
        n = len(temperatures)
        for i, val in enumerate(temperatures):
            while(stack and val > temperatures[stack[-1]]):
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans
                
                
            
                
                
        