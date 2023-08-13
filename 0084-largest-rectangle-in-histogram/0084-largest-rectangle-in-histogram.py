class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxx = 0
        n = len(heights) 
        stack = [(0,heights[0])]
        for i in range(1,len(heights)):
            if heights[i] >= heights[i-1]:
                stack.append((i, heights[i]))
            else:
                while( stack and heights[i] < stack[-1][1] ):
                    popy = stack.pop()
                    start = popy[0]
                    maxx = max(maxx, popy[1] * (i - start ))
                stack.append((start,heights[i]))                

        while(stack):
            popy = stack.pop()
            start = popy[0]
            maxx = max(maxx, popy[1] * ( n - start))
            
        return maxx
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#        bruteforce
        # area = 0
        # for i in range(len(heights)):
        #     minn = inf
        #     for j in range(i,len(heights)):
        #         if heights[j] < minn:
        #             minn = heights[j]
        #         area = max(area, minn * (j - i + 1))
        # return area
        