class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #feasibility condition: total time at curr eating speed has to be less than h
        #then we can consider it as a possible min_eating_speed

        #ordered search space = [1, max(piles)]
        #we are trying to locate eating speeds

        l, r = 1, max(piles)
        min_eating_speed = max(piles)

        while l <= r:
            m = (l + r) // 2

            total_h = 0
            for pile in piles:
                total_h += math.ceil(pile / m)
            
            print("eating speed: ", m)
            print("total hours: ", total_h)
            
            if total_h > h:
                l = m+1
            else:
                min_eating_speed = min(min_eating_speed, m)
                r = m-1
        
        return min_eating_speed

