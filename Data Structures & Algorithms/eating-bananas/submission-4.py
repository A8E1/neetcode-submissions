class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = float("infinity")
        l, r = 1, max(piles)

        while l <= r:
            h_in_total = 0

            mid = (l+r) // 2

            for pile in piles:
                h_in_total += math.ceil(pile / mid)
            
            if h_in_total <= h:
                r = mid - 1
                min_speed = min(min_speed, mid) 
            elif h_in_total > h:
                l = mid + 1
            

        return min_speed