class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        min_speed = float('infinity')

        while l <= r:
            mid = (l + r) // 2

            total_h_at_mid = 0
            
            for pile in piles:
                total_h_at_mid += math.ceil(pile / mid)
            
            if total_h_at_mid <= h:
                min_speed = min(min_speed, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return min_speed

        