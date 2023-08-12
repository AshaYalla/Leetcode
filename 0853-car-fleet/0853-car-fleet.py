class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos = [(position[i], speed[i]) for i in range(len(position))]
        pos.sort()
        
        
        time = [ (target - i[0]) / i[1] for i in pos]
        print(time)
        
        
        ans = 0
        while(len(time) >=2):
            a = time.pop()
            if time[-1] <= a:
                time[-1] = a
            else:
                ans+=1
        print(time)
        return ans + len(time)

                
                
