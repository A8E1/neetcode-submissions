class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        min_speed = float('infinity')

        while l <= r:
            mid = (l + r) // 2
            total_hours = 0

            for pile in piles:
                total_hours += math.ceil(pile / mid)
            
            if total_hours <= h:
                min_speed = min(min_speed, mid)
                r = mid - 1
            elif total_hours > h:
                l = mid + 1
        
        return min_speed

