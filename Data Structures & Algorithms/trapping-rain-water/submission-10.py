class Solution:
    def trap(self, height: List[int]) -> int:

        water = 0
        l, r = 0, len(height)-1
        max_left = height[l]
        max_right = height[r]

        while l < r:
            if max_right < max_left:
                r-=1
                max_right = max(max_right, height[r])
                water += max_right - height[r]
            else:
                l+=1
                max_left = max(max_left, height[l])
                water += max_left - height[l]


        
        return water
        