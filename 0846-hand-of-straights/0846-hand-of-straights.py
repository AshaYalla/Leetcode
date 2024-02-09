class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = collections.Counter(hand)
        for i in sorted(c):
            if c[i] > 0:
                req = c[i]
                for j in range(groupSize):
                    if c[i+j] >= req:
                        c[i+j] = c[i+j] - req
                    else:
                        return False
        return True
                
        