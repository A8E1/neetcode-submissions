class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)

        min_eater_speed = -1
        while l <= r:
            eating_speed = (l + r) // 2
            eating_time = 0
            feas = False
            for pile in piles:
                
                eating_time += math.ceil(pile / eating_speed)


            
            if eating_time > h:
                l = eating_speed+1
            else:
                min_eater_speed = eating_speed
                r = eating_speed-1
        
        return min_eater_speed




