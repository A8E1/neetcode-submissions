class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        left_max, right_max = height[l], height[r]
        water = 0

        if not height:
            return water

        while l < r:
            if right_max < left_max:
                r-=1
                right_max = max(right_max, height[r])
                water += right_max - height[r]
            else:
                l+=1
                left_max = max(left_max, height[l])
                water += left_max - height[l]
        
        return water
        