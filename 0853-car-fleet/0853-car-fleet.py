class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for d, s in sorted(zip(position, speed)):
            while stack and stack[-1] <= (target-d)/s:
                stack.pop()
            stack.append((target-d)/s)
                
        return len(stack)
                
            
              
