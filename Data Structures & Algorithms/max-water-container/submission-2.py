class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #if calc area > curr area, move ptr
            #do this for b4 moving left & right
        

        maxArea = 0
        l, r = 0, len(heights)-1

        while l < r:
            curr_area = min(heights[l], heights[r]) * (r-l)
            maxArea = max(curr_area, maxArea)

            if l < len(heights)-1 and curr_area < (min(heights[l+1], heights[r]) * (r-(l+1))):
                l+=1
                continue
            
            if r > 0 and curr_area < (min(heights[l], heights[r-1]) * ((r-1)-l)):
                r-=1
                continue
            
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1

        #[1, 2, 9, 3, 4, 1, 7]
            

            

        return maxArea

            

