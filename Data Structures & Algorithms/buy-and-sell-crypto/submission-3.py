class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        starter_price = prices[0]
        for r in range(len(prices)):
            if prices[r] < starter_price:
                starter_price = prices[r]
            else: 
                max_profit = max(max_profit, prices[r] - starter_price)
        
        return max_profit
            
