class Solution:
    def minMoves(self, target: int, maxDoubles: int, steps=0) -> int:

        if target == 1:
            return steps
        
        if maxDoubles == 0:
            return self.minMoves(target - target + 1, maxDoubles, steps + target - 1)

        if target%2 == 0 and maxDoubles != 0:
            return self.minMoves(int(target / 2), maxDoubles - 1, steps + 1)
        else:
            return self.minMoves(target - 1, maxDoubles, steps + 1)