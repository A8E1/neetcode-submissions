class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        l, r = 0, len(heights)-1

        while l < r:

            curArea = (r-l) * min(heights[l], heights[r])

            max_area = max(max_area, curArea)

            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        
        return max_area