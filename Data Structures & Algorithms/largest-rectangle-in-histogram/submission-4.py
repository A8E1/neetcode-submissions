class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for ind, height in enumerate(heights):

            start = ind
            while stack and height < stack[-1][1]:
                popped_start, popped_height = stack.pop()

                maxArea = max(maxArea, (popped_height * (ind-popped_start)))

                start = popped_start
            
            stack.append([start, height])
        
        while stack:
            popped_start, popped_height = stack.pop()

            maxArea = max(maxArea, (popped_height * (len(heights)-popped_start)))
        
        return maxArea
