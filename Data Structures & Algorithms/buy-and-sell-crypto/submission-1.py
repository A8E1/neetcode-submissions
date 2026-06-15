class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        best_buy = prices[0]
        for R in range(1, len(prices)):
            if best_buy > prices[R]:
                best_buy = prices[R]

            cur_profit = prices[R] - best_buy

            max_profit = max(max_profit, cur_profit)

        return max_profit
    