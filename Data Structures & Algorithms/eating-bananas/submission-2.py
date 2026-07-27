class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        print(r)
        min_eating_speed = r

        while l <= r:
            mid = (l + r) // 2
            total_hrs = 0
            for pile in piles:
                total_hrs += math.ceil(pile / mid)
            
            if total_hrs > h:
                l = mid + 1
            elif total_hrs <= h:
                r = mid - 1
                min_eating_speed = min(min_eating_speed, mid)
            
        return min_eating_speed
