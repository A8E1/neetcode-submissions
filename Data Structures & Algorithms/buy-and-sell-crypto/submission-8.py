class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_prof = 0

        for r in range(len(prices)):

            if prices[r] < prices[l]:
                l = r
            
            max_prof = max(max_prof, prices[r] - prices[l])
        
        return max_prof
        