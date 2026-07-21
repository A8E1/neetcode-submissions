class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        best_buy = prices[0]

        l = 0
        for r in range(len(prices)):

            if prices[r] < best_buy:
                best_buy = prices[r]
                l = r
            
            maxProfit = max(maxProfit, prices[r] - prices[l])
        
        return maxProfit
            
        