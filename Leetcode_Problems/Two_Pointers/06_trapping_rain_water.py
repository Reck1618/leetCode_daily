"""
"""

# solution 1
class Solution:
    def trap(self, height):
        res = 0
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]

        while l < r:
            if height[l] <= height[r]:
                water = max_l - height[l]
                max_l = max(max_l, height[l])
                if water > 0:
                    res += water
                l += 1
            else:
                water = max_r - height[r]
                max_r = max(max_r, height[r])
                if water > 0:
                    res += water
                r -= 1
        return res

# solution 2
class Solution:
    def trap(self, height):
        res = 0
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]

        while l < r:
            if max_l <= max_r:
                l += 1
                max_l = max(max_l, height[l])
                res += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                res += max_r - height[r]
        return res
