class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        best_buy_idx = 0

        for sell_price_idx in range(0, len(prices)):

            if prices[best_buy_idx] > prices[sell_price_idx]:
                best_buy_idx = sell_price_idx
            
            maxProfit = max(maxProfit, (prices[sell_price_idx] - prices[best_buy_idx]))
        
        return maxProfit
