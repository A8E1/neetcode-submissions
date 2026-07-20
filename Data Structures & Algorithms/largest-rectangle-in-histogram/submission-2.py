class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

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

