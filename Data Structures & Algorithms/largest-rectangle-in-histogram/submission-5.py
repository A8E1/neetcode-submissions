class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        max_area = 0

        for ind, height in enumerate(heights):
            curr_start = ind

            while stack and stack[-1][1] > height:
                popped_start, popped_height = stack.pop()

                curr_start = popped_start

                max_area = max(max_area, popped_height * (ind - popped_start))
            
            stack.append([curr_start, height])
        

        while stack:
            popped_start, popped_height = stack.pop()
            max_area = max(max_area, popped_height * (len(heights) - popped_start))
        
        
        return max_area

        