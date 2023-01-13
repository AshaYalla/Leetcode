class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        j = 0
        for i in range(1,len(prices)):
            if(prices[i] < prices[j]):
                j = i
            maxi = max(maxi,prices[i] - prices[j])
            
        return maxi
            