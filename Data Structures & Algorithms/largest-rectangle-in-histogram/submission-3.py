class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        #stack stores tuples of (start_ind, height)

        #rectangle area of a certain bar height is capped once a bar comes along that is shorter than it
        #that new bar's height can start at the old bar height's start, or if the bar height is already stored with 
        #an older start index, then we skip recording the new bar since it's height is already accounted for

        for ind, height in enumerate(heights):
            start = ind
            while stack and stack[-1][1] > height:
                popped_start, popped_height = stack.pop()

                maxArea = max(maxArea, (ind - popped_start) * popped_height)

                start = popped_start
            
            if stack and stack[-1][1] == height:
                continue
            
            stack.append((start, height))
        
        while stack:
            popped_start, popped_height = stack.pop()
            maxArea = max(maxArea, (len(heights) - popped_start) * popped_height)
        
        return maxArea
