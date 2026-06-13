class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height)-1
        left_max, right_max = height[l], height[r]
        water = 0

        while l < r:
            if right_max < left_max:
                i = r-1
                right_max = max(right_max, height[i])
                water += right_max - height[i]
                r -= 1
            else:
                i = l+1
                left_max = max(left_max, height[i])
                water += left_max - height[i]
                l += 1

        return water
