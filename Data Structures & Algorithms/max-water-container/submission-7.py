class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #water calc = (shorter bar height to avoid spilling) min(height[r], height[l]) * r-l (distance btwn l and r)

        maxWater = 0

        l, r = 0, len(heights)-1

        while l < r:
            currWater = min(heights[l], heights[r]) * (r-l)
            maxWater = max(maxWater, currWater)

            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1

        return maxWater